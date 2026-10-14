"""
This is the entry point into the application.
Handles:
    Loading schema
    Running the reasoner
    Handle asserted vs inferred facts
    
    routes user actions to related queries in queries.py
    
    python app.py   ->  http://127.0.0.1:5000
"""

# =========================
# IMPORTS
# =========================
from flask import Flask, abort, render_template, request
from owlready2 import *

import config
from utility import utils
import queries
from datasets import Dataset

# =========================
# SETTINGS
# =========================
SCHEMAS = ["test_base"]
DATASET = Dataset(config.DEFAULT_DATASET)
INFERRED_IRI = "http://uwa/uni.inferred#"
 
# Browse section -> schema class name.
BROWSABLE = {
    "degrees": "Degree",
    "majors": "Major",
    "units": "Unit",
}


# =========================
# KNOWLEDGE BASE
# =========================
class KnowledgeBase:
    """
    This is the core of the applicaiton so it owns 
    all the required data to run and work from.
    
    """

    def __init__(self, schema_names: list[str], dataset: Dataset):
        self.schema_names = schema_names
        self.dataset = dataset
        self.world = World()           # RULE: everything goes through this world
        self.schemas = []
        self.graph = None
        self.inferred = None
        self.notices = []              # status messages shown on the home page
        self.reasoning_error = None
        self.asserted_types = {}       # individual -> set of classes before reasoning
        self.asserted_values = {}      # individual -> {property: set of values}
        self.engine = None
        
    def load(self):
        self.schemas = utils.load_schemas(self.world, self.schema_names)
        if self.dataset.is_built():
            self.graph = utils.load_graph(self.world, self.dataset)
        else:
            self.notices.append(f"No graph built for dataset '{self.dataset.name}' yet. "
                                "Showing the schema only.")
            
        self._snapshot_asserted()
        self._reason()
        self.engine = queries.QueryEngine(self.world, data_iri=self.dataset.iri)
 
    def _snapshot_asserted(self):
        for ind in self.world.individuals():
            self.asserted_types[ind] = set(ind.is_a)
            self.asserted_values[ind] = {prop: set(prop[ind]) for prop in ind.get_properties()}
 
    def _reason(self):
        self.inferred = self.world.get_ontology(INFERRED_IRI)
        try:
            utils.run_reasoner(self.world, store_in=self.inferred)
        except OwlReadyInconsistentOntologyError:
            self.reasoning_error = ("The ontology is inconsistent with this data. No inferences were added.")
        except Exception as exc:
            self.reasoning_error = (f"Reasoner failed ({exc}). Check Java is installed and configured.")
 
    def cls(self, name):
        for onto in self.schemas:
            found = onto[name]
            if isinstance(found, ThingClass):
                return found
        return None

    def describe(self, entity):
        """Split an individual's types and property values into asserted vs inferred."""
        before_types = self.asserted_types.get(entity, set())
        before_values = self.asserted_values.get(entity, {})
        types = {
            "asserted": sorted(before_types, key=str),
            "inferred": sorted(set(entity.is_a) - before_types, key=str),
        }
        properties = []
        for prop in sorted(entity.get_properties(), key=lambda p: p.name):
            before = before_values.get(prop, set())
            for value in sorted(set(prop[entity]), key=str):
                properties.append((prop, value, "asserted" if value in before else "inferred"))
        return types, properties

# =========================
# DISPLAY HELPERS
# =========================
def cell(value) -> queries.Cell:
    """Entity -> (name, iri) so it becomes a link; anything else -> plain text."""
    if hasattr(value, "iri"):
        return (getattr(value, "name", str(value)), value.iri)
    return (str(value), None)


def text(value) -> queries.Cell:
    return (str(value), None)


def names(items) -> str:
    """Readable comma list of classes / datatypes (e.g. a domain or range)."""
    return ", ".join(getattr(i, "name", None) or getattr(i, "__name__", str(i)) for i in items)
 

def characteristics(prop) -> str:
    """Functional, transitive, etc., plus the inverse if there is one."""
    found = [c.__name__ for c in prop.is_a
             if isinstance(c, type) and c.__name__.endswith("Property")
             and c.__name__ not in ("ObjectProperty", "DataProperty")]
    if getattr(prop, "inverse_property", None):
        found.append(f"inverse of {prop.inverse_property.name}")
    return ", ".join(found)
 
def section(heading=None, headers=(), rows=(), message=None, ok=True):
    return {"heading": heading, "headers": list(headers), "rows": list(rows),
            "message": message, "ok": ok}
 
def result_section(heading, result: queries.QueryResult):
    return section(heading, result.headers, result.rows, result.message, result.ok)
 
def render(title, sections=(), notices=(), form=None):
    return render_template("page.html", title=title, sections=sections,
                           notices=list(notices), form=form)


# =========================
# APP + ROUTES
# =========================
app = Flask(__name__, template_folder="../frontend", static_folder="../frontend")
kb = KnowledgeBase(SCHEMAS, DATASET)
kb.load()


# Create list of browsable objects
@app.context_processor
def nav_context():
    return {"browsable": BROWSABLE}
 
 
# This is the home page. routing just adds a pages essentially
# eg. http:// | 127.0.0.1 |:5000 |/page
#    |protocol|Domain|Port|Page
# we add a function after to run when that specific URL is reached
# You always reach "/" so this is the home page
@app.route("/")
def home():
    rows = []
    for key, class_name in BROWSABLE.items():
        cls = kb.cls(class_name)
        count = len(list(cls.instances())) if cls else "class not found"
        rows.append([text(key.capitalize()), text(count)])
 
    loaded = [[text(name), text(onto.base_iri)] for name, onto in zip(kb.schema_names, kb.schemas)]
    status = kb.reasoning_error or f"Reasoner ({config.REASONER}) ran successfully."
    return render("Handbook knowledge graph", [
        section("Entities", ["Section", "Count"], rows),
        section("Loaded schemas", ["Schema", "IRI"], loaded),
    ], notices=[status, *kb.notices])


# Display the schema
@app.route("/schema")
def schema():
    sections = []
    for name, onto in zip(kb.schema_names, kb.schemas):
        class_rows = [[cell(c),
                       text(names(p for p in c.is_a if isinstance(p, ThingClass))),
                       text(len(list(c.instances())))]
                      for c in sorted(onto.classes(), key=lambda c: c.name)]
        object_rows = [[cell(p), text(names(p.domain)), text(names(p.range)), text(characteristics(p))]
                       for p in sorted(onto.object_properties(), key=lambda p: p.name)]
        data_rows = [[cell(p), text(names(p.domain)), text(names(p.range)), text(characteristics(p))]
                     for p in sorted(onto.data_properties(), key=lambda p: p.name)]
        individual_rows = [[cell(i), text(names(i.is_a))]
                           for i in sorted(onto.individuals(), key=lambda i: i.name)]
        rule_rows = [[text(r)] for r in onto.rules()]
 
        sections += [
            section(f"{name}: classes", ["Class", "Parents", "Instances"], class_rows,
                    f"{len(class_rows)} classes"),
            section(f"{name}: object properties", ["Property", "Domain", "Range", "Characteristics"],
                    object_rows, f"{len(object_rows)} object properties"),
            section(f"{name}: data properties", ["Property", "Domain", "Range", "Characteristics"],
                    data_rows, f"{len(data_rows)} data properties"),
            section(f"{name}: individuals", ["Individual", "Types"], individual_rows,
                    f"{len(individual_rows)} individuals"),
            section(f"{name}: rules", ["Rule"], rule_rows, f"{len(rule_rows)} rules"),
        ]
    return render("Schema", sections)
 

@app.route("/browse/<kind>")
def browse(kind):
    class_name = BROWSABLE.get(kind) or abort(404)
    cls = kb.cls(class_name)
    if cls is None:
        return render(kind.capitalize(), notices=[f"Class '{class_name}' not found in the schema."])
 
    q = request.args.get("q", "").strip()
    items = sorted(cls.instances(), key=lambda e: e.name)
    if q:
        needle = q.lower()
        items = [e for e in items
                 if needle in e.name.lower() or any(needle in str(l).lower() for l in e.label)]
 
    rows = [[cell(e), text(", ".join(map(str, e.label)))] for e in items]
    return render(kind.capitalize(),
                  [section(None, ["Entity", "Label"], rows, f"{len(rows)} entities")],
                  form={"kind": "filter", "q": q})

@app.route("/entity")
def entity():
    iri = request.args.get("iri", "")
    target = kb.world[iri] if iri else None
    if target is None:
        abort(404)
 
    if isinstance(target, ThingClass):
        rows = [[cell(i)] for i in sorted(target.instances(), key=lambda e: e.name)]
        return render(f"Class: {target.name}",
                      [section("Instances (asserted + inferred)", ["Individual"], rows,
                               f"{len(rows)} instances")], notices=[target.iri])
 
    if not isinstance(target, Thing):
        return render(getattr(target, "name", iri),
                      notices=[f"{iri}: no detail view for this kind of entity."])
 
    types, props = kb.describe(target)
    type_rows = ([[cell(t), text("asserted")] for t in types["asserted"]] +
                 [[cell(t), text("inferred")] for t in types["inferred"]])
    prop_rows = [[cell(p), cell(v), text(source)] for p, v, source in props]
    return render(target.name, [
        section("Types", ["Class", "Source"], type_rows),
        section("Properties", ["Property", "Value", "Source"], prop_rows),
    ], notices=[target.iri])
 
 
@app.route("/search")
def search():
    q = request.args.get("q", "").strip()
    form = {"kind": "search", "q": q}
    if not q:
        return render("Search", form=form)
 
    found = set(kb.world.search(iri=f"*{q}*", _case_sensitive=False))
    found |= set(kb.world.search(label=f"*{q}*", _case_sensitive=False))
    entity_rows = [[cell(e)] for e in sorted(found, key=lambda e: getattr(e, "name", str(e)))]
 
    outcomes = queries.run_named(queries.NAMED_QUERIES, "outcome_search", kb.engine, text=q)
    return render("Search", [
        section("Entities matching name or label", ["Entity"], entity_rows,
                f"{len(entity_rows)} match(es)"),
        result_section("Majors with matching outcomes", outcomes),
    ], form=form)
 
 
@app.route("/query")
def run_query():
    key = request.args.get("name", "")
    sparql = request.args.get("sparql", "").strip()
    params = {k: v for k, v in request.args.items() if k not in ("name", "sparql")}
 
    form = {"kind": "query", "named": list(queries.NAMED_QUERIES.values()), "key": key,
            "params": params, "sparql": sparql, "prefixes": kb.engine.prefix_block()}
    sections = []
    if key:
        title = queries.NAMED_QUERIES[key].title if key in queries.NAMED_QUERIES else key
        result = queries.run_named(queries.NAMED_QUERIES, key, kb.engine, **params)
        sections.append(result_section(title, result))
    elif sparql:
        sections.append(result_section("SPARQL result", kb.engine.run(sparql)))
    return render("Query", sections, form=form)
 
 
@app.route("/errors")
def errors():
    sections = [section("Reasoner",
                        message=kb.reasoning_error or "The ontology is consistent with the data.",
                        ok=kb.reasoning_error is None)]
 
    unsatisfiable = list(kb.world.inconsistent_classes())
    sections.append(section("Unsatisfiable classes", ["Class"],
                            [[cell(c)] for c in unsatisfiable],
                            f"{len(unsatisfiable)} found", ok=not unsatisfiable))
 
    for nq in queries.ERROR_CHECKS.values():
        result = queries.run_named(queries.ERROR_CHECKS, nq.key, kb.engine)
        sections.append(result_section(nq.title, result))
    return render("Data errors", sections)
 
 
if __name__ == "__main__":
    # use_reloader=False: the debug reloader would load and reason twice.
    # threaded=False: owlready2 isn't thread-safe; one request at a time is fine here.
    app.run(debug=True, use_reloader=False, threaded=False)