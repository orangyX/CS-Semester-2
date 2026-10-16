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
from collections import Counter, defaultdict

import re
import inspect

import rdflib
from flask import Flask, abort, redirect, render_template, request, url_for
from rdflib import Literal, URIRef

import main as pipeline
import queries
from utility import config, utils
from utility.caching import Cache
from utility.datasets import Dataset


# =========================
# SETTINGS
# =========================
Q = queries.MakeQueries

DATASET = Dataset(config.DATASET_NAME)
SCHEMAS = [config.SCHEMA_NAME, config.RULES_NAME]
CACHE = Cache(DATASET)

ASSERTED = rdflib.Graph()     
GRAPH = rdflib.Graph()        
ERRORS = Counter()
ERRORS_BEFORE = Counter()

TITLE = LEVEL = CREDIT = SCHOOL = STUDY_TYPE = {}
BINDING = re.compile(r"\?(selected\w+|searchTerm)\b")
SCHEMA_PARAMS = ("selectedType", "selectedPredicate", "selectedRelation")

# =========================
# App entry
# =========================

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend")



# =========================
# These are a bunch of helpers that have come out of trying to make
# functions work. :'(
# =========================
def table(title, columns, rows):
    return render_template("results.html", title=title, columns=columns, rows=rows)

def run(sparql, graph=None, **bindings):
    if graph is None:
        graph = GRAPH      
    return queries.run(graph, DATASET, sparql, **bindings)

def uni(name):
    """
    Convert a schema value into a IRI
    """
    return URIRef(config.SCHEMA_IRI + name)

def data(name):
    """
    Convert a dataset value into a IRI
    """
    return URIRef(DATASET.iri + name)

def column(prop):
    rows = run(Q.query_by_relation(), selectedRelation=uni(prop))
    return {subject: obj for subject, _relation, obj in rows}

def facts(name, graph=None):
    result = defaultdict(list)
    for _entity, prop, value in run(Q.get_outgoing(), graph, selectedEntity=data(name)):
        result[prop].append(value)
    return result

def first(values):
    return values[0] if values else ""

def unit_row(name):
    return {"code": name, "title": TITLE.get(name, ""),
            "level": LEVEL.get(name, ""), "credit": CREDIT.get(name, "")}

def major_row(name):
    return {"code": name, "title": TITLE.get(name, ""), "school": SCHOOL.get(name, "")}

def schema_term(name):
    for namespace in (config.SCHEMA_IRI, config.RULES_IRI):
        term = URIRef(namespace + name)
        if (term, None, None) in GRAPH or (None, term, None) in GRAPH or (None, None, term) in GRAPH:
            return term
    abort(404)
    
def binding(param, value):
    """
    Attempt to match the input to some kind of known IRI
    """
    if value.startswith("uni:"):
        return uni(value[4:])
    if value.startswith("data:"):
        return data(value[5:])
    if value.isdigit():
        return Literal(int(value))
    
    # Which namespace to try first depends on what the binding is for
    if param in SCHEMA_PARAMS:
        makers = (uni, data)
    else:
        makers = (data, uni)

    for make in makers:
        for name in (value, value.upper()): 
            term = make(name)
            if in_graph(term):
                return term

    return Literal(value)    

def in_graph(term):
    """
    True if the term appears anywhere in the graph (as subject, property or object).
    """
    return ((term, None, None) in GRAPH
            or (None, term, None) in GRAPH
            or (None, None, term) in GRAPH)

@app.context_processor
def check_loaded():
    """
    Small fix for flag that resets every page change.
    """
    return {"loaded": len(GRAPH) > 0, "built": DATASET.is_built()}
# =========================
# END POINTS
# =========================

# Load front page
# Initially nothing loads into the system and must be manually triggered.
# 
@app.route("/")
def home():
    return render_template("home.html", built=DATASET.is_built(), loaded=len(GRAPH) > 0)

@app.route("/rebuild", methods=["POST"])
def rebuild():
    """
    This comes from main and just builds the graph using a schema from 
    the data set. RN this is all hardcoded with expecte files etc
    
    It actually uses 2 places so modifying could break alot
    
    In main it pulls its description and from header of this file is
    used to load it. 
    
    Theres the foundation for being to load different datasets with different
    ontologies.
    """
    pipeline.build()
    return redirect(url_for("home"))

@app.route("/reason", methods=["POST"])
def load():
    """
    Load all the information ready for app to use.
    This pulls the 2 graphs asserted and inferred and other objects like errors from shapes
    """
    global ASSERTED, GRAPH, ERRORS, ERRORS_BEFORE, TITLE, LEVEL, CREDIT, SCHOOL, STUDY_TYPE
    
    ASSERTED, GRAPH, ERRORS, ERRORS_BEFORE = pipeline.reason(DATASET, SCHEMAS)
    
    # Basic relations that ALWAYS get returned with an object 
    # CITS3005 -> return title, level etc.
    TITLE = column("hasTitle")
    LEVEL = column("hasLevel")
    CREDIT = column("hasCredit")
    SCHOOL = column("belongsTo")
    STUDY_TYPE = column("hasStudyType")
    
    return redirect(url_for("home"))
    
@app.route("/search")
def search():
    """
    Logic for search page
    allow a search query to try find ANY objects that contain the 
    search term.
    
    Also allow filters to be added to the page.
    """
    q = request.args.get("q", "").strip()
    fields = request.args.getlist("field")   
    values = request.args.getlist("value")
    
    rows = run(Q.search_all(), searchTerm=Literal(q)) if q else []
    
    for field, value in zip(fields, values):
        value = value.strip()
        if not field or not value:
            continue     
                           
        keep = set()
        for match in run(Q.filter_contains(),
                         selectedPredicate=uni(field),
                         searchTerm=Literal(value)):
            entity = match[0]
            keep.add(entity)
            
        rows = [row for row in rows if row[0] in keep]
    return render_template("search.html", q=q, columns=["Entity", "Title", "Property", "Value"], rows=rows)
    # return table(f'Result for "{q}"', ["Entity", "Title", "Property", "Value"], rows)

def available_queries():
    """
    Find every query available in query class and return ans a name
    """
    result = []
    for name, method in inspect.getmembers(Q, inspect.isfunction):
        if name.startswith("_"):
            continue
        sparql = method()
        result.append({
            "name": name,
            "description": (method.__doc__ or "").strip(),
            "params": sorted(set(BINDING.findall(sparql))),
        })
    return result

@app.route("/query")
def query():
    """
    List available querys to make against the graph
    """
    return render_template("queries.html", queries=available_queries())

@app.route("/query/<name>")
def run_query(name):
    """
    Attempt to run a query and attempt to match a binding for it. 
    It's a little unintuitive so we might need to specify in user manual 
    or find a way to display what is available to search for. 
    """
    method = getattr(Q, name, None)
    if name.startswith("_") or not callable(method):
        abort(404)

    sparql = method()
    bindings = {}
    for param in set(BINDING.findall(sparql)):
        value = request.args.get(param, "").strip()
        if value:
            bindings[param] = binding(param, value)

    return table(name, queries.headers(DATASET, sparql), run(sparql, **bindings))

@app.route("/query/count")
def query_count():
    """
    Count how many of each class are in the graph.
    """
    return table("Counts", ["Class", "Count"], run(Q.count_all_entities()))


@app.route("/query/inferred/<name>")
def inferred_facts(name):
    """
    Ask what objects are inferred or added by the reasoner.
    """
    before = set(run(Q.get_incoming(), ASSERTED, selectedEntity=data(name)))  
    after  = run(Q.get_incoming(), GRAPH, selectedEntity=data(name))  

    rows = []
    for subject, prop in after:
        if (subject, prop) not in before:
            rows.append((subject, prop))

    return table(f"Infered facts pointing at {name}", ["Subject", "Property"], rows)

@app.route("/query/asserted/<name>")
def asserted_facts(name):
    """
    Ask what objects are asserted 
    """
    rows = run(Q.get_incoming(), ASSERTED, selectedEntity=data(name))  
    return table(f"Asserted facts pointing at {name}", ["Subject", "Property"], rows)


@app.route("/query/classes/<name>")
def entity_classes(name):
    """
    Every class an entity belongs to asserted or inferred
    """
    before = set(run(Q.get_parents(), ASSERTED, selectedEntity=data(name)))
    after = run(Q.get_parents(), GRAPH, selectedEntity=data(name))

    rows = []
    for (cls,) in after:
        source = "asserted" if (cls,) in before else "inferred"
        rows.append((cls, source))

    return table(f"Classes of {name}", ["Class", "Source"], rows)

@app.route("/query/classes")
def inferred_classes():
    """
    Every entity thats inferred
    """
    before = set(run(Q.query_by_relation(), ASSERTED, selectedRelation=rdflib.RDF.type))
    after = run(Q.query_by_relation(), GRAPH, selectedRelation=rdflib.RDF.type)

    rows = []
    for entity, cls in after:
        if (entity, cls) not in before:
            rows.append((entity, cls))

    return table("Inferred classes", ["Entity", "Inferred class"], rows)

@app.route("/validation")
def validation():
    """SHACL problems before and after reasoning."""
    rows = []
    for message in sorted(set(ERRORS_BEFORE) | set(ERRORS)):
        rows.append((message, ERRORS_BEFORE.get(message, 0), ERRORS.get(message, 0)))
    return table("Data validation", ["Problem", "Before reasoning", "After reasoning"], rows)

@app.route("/browse/classes")
def browse_class():
    classes = [{"name": name, "count": count} for name, count in run(Q.count_all_entities())]
    return render_template("data/class.html", classes=classes)


@app.route("/browse/class/<name>")
def class_members(name):
    members = [{"name": entity, "title": title}
               for entity, title in run(Q.list_members(), selectedType=schema_term(name))]
    return render_template("data/members.html", cls=name, members=members)

@app.route("/browse/property")
def browse_property():
    properties = [{"name": name, "count": count} for name, count in run(Q.count_all_relations())]
    return render_template("data/properties.html", properties=properties)


@app.route("/browse/property/<name>")
def property_pairs(name):
    pairs = [{"subject": subject, "value": obj}
             for subject, _relation, obj in run(Q.query_by_relation(), selectedRelation=schema_term(name))]
    return render_template("data/pairs.html", prop=name, pairs=pairs)

@app.route("/browse/degrees")
def browse_degrees():
    degrees = []
    for name, title in run(Q.list_members(), selectedType=uni("Degree")):
        if title:
            degrees.append({"code": name, "title": title,
                            "study_type": STUDY_TYPE.get(name, "")})
    return render_template("data/degree.html", degrees=degrees)

@app.route("/browse/major")
def browse_majors():
    """
    Every major with its school.
    """
    majors = []
    for name, title in run(Q.list_members(), selectedType=uni("Major")):
        majors.append(major_row(name))
    return render_template("data/major.html", majors=majors)


@app.route("/browse/units")
def browse_units():
    """
    Every unit with its level and credit points.
    Units only referenced as prerequisites (no title) are skipped.
    """
    units = []
    for name, title in run(Q.list_members(), selectedType=uni("Unit")):
        if title:
            units.append(unit_row(name))
    return render_template("data/unit.html", units=units)

@app.route("/browse/degree/<code>")
def degree_details(code):
    f = facts(code)
    if not f:
        abort(404)
    degree = {
        "code": code,
        "title": first(f["hasTitle"]),
        "study_type": first(f["hasStudyType"]),
        "points": first(f["hasTotalPoints"]),
        "majors": [major_row(m) for m in sorted(set(f["hasMajor"]))],
    }
    return render_template("details/degree.html", degree=degree)

@app.route("/browse/major/<code>")
def major_details(code):
    f = facts(code)
    if not f:
        abort(404)
    major = {
        "code": code,
        "title": first(f["hasTitle"]),
        "school": first(f["belongsTo"]),
        "units": [unit_row(u) for u in sorted(set(f["hasUnit"]))],
    }
    return render_template("details/major.html", major=major)

@app.route("/browse/unit/<code>")
def unit_details(code):
    f = facts(code)
    if not f:
        abort(404)
    direct = facts(code, ASSERTED)["hasPrerequisite"]     
    every = f["hasPrerequisite"]                          
    unit = unit_row(code)
    unit["direct_prereqs"] = [unit_row(p) for p in sorted(set(direct))]
    unit["all_prereqs"] = [unit_row(p) for p in sorted(set(every))]
    return render_template("details/unit.html", unit=unit)

    
# =========================
# SPEC QUERIES 
# These are just the specified queries from the task sheet
# =========================
@app.route("/spec/foundational")
def spec_foundational():
    degree = request.args.get("degree", "").strip()
    bindings = {"selectedDegree": data(degree)} if degree else {}
    rows = run(Q.foundational_units(), **bindings)
    return table("Foundational units by degree", ["Degree", "Unit"], rows)

@app.route("/spec/average-majors")
def spec_average_majors():
    rows = run(Q.average_majors())
    return table("Average majors per degree type (excluding BPhil)", ["Degree type", "Average majors"], rows)

@app.route("/spec/location")
def spec_location():
    place = request.args.get("location", "").strip() or "Albany"
    rows = run(Q.majors_in_location(), selectedLocation=data("Location_" + utils.slug(place)))
    return table(f"Majors completable in {place}", ["Major", "Title"], rows)

@app.route("/spec/outcomes")
def spec_outcomes():
    text = request.args.get("q", "").strip() or "data analysis"
    rows = run(Q.outcome_search(), searchTerm=Literal(text))
    return table(f'Majors with outcomes matching "{text}"', ["Major", "Title", "Outcome"], rows)
    
    
if __name__ == "__main__":
    # Apparently port 5000 is taken on Mac so using 5001
    app.run(debug=True, use_reloader=False, threaded=False, port=5001)