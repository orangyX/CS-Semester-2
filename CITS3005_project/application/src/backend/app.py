"""
app.py - Flask interface for browsing and querying the UWA handbook knowledge graph.

ROLE
    User interaction only. This file:
      - loads the schema + KG once at startup and runs the reasoner once,
      - remembers what was *asserted* before reasoning, so pages can show
        asserted vs inferred facts separately (spec requirement),
      - routes user actions to queries.py and displays the results.
    No SPARQL lives here; all questions go through queries.py.

DECISIONS
    - Read-only: the app never edits the graph. Adding/updating data = edit the
      dataset and rebuild with build_kg.py. Avoids owlready2 thread-safety
      issues and keeps the manual's "how to change data" section simple.
    - Reason once at startup: the reasoner runs Java and is slow.
    - Inferred facts go into their own ontology (INFERRED_IRI), never into
      the schema or data files.
    - Pages use one inline template for now.  OPEN: move to templates/ later.

EXPECTED IN config.py
    OUTPUT_DIR, SCHEMA_FILE                 (absolute Path objects)
    DATA_FILES (list of Paths) or DATA_FILE (single Path)
    optional: INFERRED_IRI, REASONER ("hermit" | "pellet"), BROWSABLE

RUN
    python app.py   ->  http://127.0.0.1:5000
"""

# =========================
# IMPORTS
# =========================
from flask import Flask, abort, render_template_string, request
from owlready2 import *

import config
import queries

# =========================
# SETTINGS
# =========================
IRI = getattr(config, "IRI", "http://uwa/uni.inferred#")
REASONER = getattr(config, "REASONER", "hermit")

# Browse section -> schema class name.  OPEN: adjust to our final class names.
BROWSABLE = getattr(config, "BROWSABLE", {
    "degrees": "Degree",
    "majors": "Major",
    "units": "Unit",
})


def data_files():
    """Supports one KG file or several data modules."""
    if hasattr(config, "DATA_FILES"):
        return list(config.DATA_FILES)
    return [config.DATA_FILE]


# =========================
# KNOWLEDGE BASE
# =========================
class KnowledgeBase:

    def __init__(self):
        self.world = World()           # RULE: everything goes through this world
        self.schema = None
        self.data_ontologies = []
        self.inferred = None
        self.reasoning_error = None
        self.asserted_types = {}       # individual -> set of classes before reasoning
        self.asserted_values = {}      # individual -> {property: set of values}
        self.engine = None

    def load(self):
        onto_path.append(str(config.OUTPUT_DIR))   # lets data files resolve their schema import
        self.schema = self.world.get_ontology(config.SCHEMA_FILE.as_uri()).load()
        for path in data_files():
            self.data_ontologies.append(self.world.get_ontology(path.as_uri()).load())
        self._snapshot_asserted()
        self._reason()
        self.engine = queries.QueryEngine(self.world)

    def _snapshot_asserted(self):
        for ind in self.world.individuals():
            self.asserted_types[ind] = set(ind.is_a)
            self.asserted_values[ind] = {prop: set(prop[ind]) for prop in ind.get_properties()}

    def _reason(self):
        self.inferred = self.world.get_ontology(IRI)
        try:
            with self.inferred:   # inferred facts are stored in this ontology
                if REASONER == "pellet":
                    sync_reasoner_pellet(self.world, infer_property_values=True,
                                         infer_data_property_values=True)
                else:
                    sync_reasoner(self.world, infer_property_values=True)
        except OwlReadyInconsistentOntologyError:
            self.reasoning_error = ("The ontology is inconsistent with this data. "
                                    "No inferences were added.")
        except Exception as exc:
            self.reasoning_error = (f"Reasoner failed ({exc}). "
                                    "Check Java is installed and configured.")

    def cls(self, name):
        return getattr(self.schema, name, None)

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


def section(heading=None, headers=(), rows=(), message=None, ok=True):
    return {"heading": heading, "headers": list(headers), "rows": list(rows),
            "message": message, "ok": ok}


def result_section(heading, result: queries.QueryResult):
    return section(heading, result.headers, result.rows, result.message, result.ok)


# =========================
# APP + ROUTES
# =========================
app = Flask(__name__)
kb = KnowledgeBase()
kb.load()


@app.route("/")
def home():
    rows = []
    for key, class_name in BROWSABLE.items():
        cls = kb.cls(class_name)
        count = len(list(cls.instances())) if cls else "class not found"
        rows.append([text(key.capitalize()), text(count)])
    status = kb.reasoning_error or f"Reasoner ({REASONER}) ran successfully."
    return render("Handbook knowledge graph",
                  [section(None, ["Section", "Entities"], rows)], notice=status)


@app.route("/browse/<kind>")
def browse(kind):
    class_name = BROWSABLE.get(kind) or abort(404)
    cls = kb.cls(class_name)
    if cls is None:
        return render(kind.capitalize(), notice=f"Class '{class_name}' not found in the schema.")

    q = request.args.get("q", "").strip()
    items = sorted(cls.instances(), key=lambda e: e.name)
    if q:
        needle = q.lower()
        items = [e for e in items
                 if needle in e.name.lower() or any(needle in str(l).lower() for l in e.label)]

    rows = [[cell(e), text(", ".join(map(str, e.label)))] for e in items]
    form = render_template_string(FILTER_FORM, q=q)
    return render(kind.capitalize(),
                  [section(None, ["Entity", "Label"], rows, f"{len(rows)} entities")], form=form)


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
                               f"{len(rows)} instances")], notice=target.iri)

    if not isinstance(target, Thing):
        return render(getattr(target, "name", iri), notice=f"{iri}: no detail view for this kind of entity.")

    types, props = kb.describe(target)
    type_rows = ([[cell(t), text("asserted")] for t in types["asserted"]] +
                 [[cell(t), text("inferred")] for t in types["inferred"]])
    prop_rows = [[cell(p), cell(v), text(source)] for p, v, source in props]
    return render(target.name, [
        section("Types", ["Class", "Source"], type_rows),
        section("Properties", ["Property", "Value", "Source"], prop_rows),
    ], notice=target.iri)


@app.route("/search")
def search():
    q = request.args.get("q", "").strip()
    form = render_template_string(SEARCH_FORM, q=q)
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

    form = render_template_string(QUERY_FORM, named=queries.NAMED_QUERIES.values(), key=key,
                                  params=params, sparql=sparql,
                                  prefixes=kb.engine.prefix_block())
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
