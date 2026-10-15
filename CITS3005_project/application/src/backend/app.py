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

import rdflib
from flask import Flask, abort, redirect, render_template, request, url_for
from rdflib import Literal, URIRef

import main as pipeline
import queries
from shapes import shapes
from utility import config, utils
from utility.datasets import Dataset


# =========================
# SETTINGS
# =========================
Q = queries.MakeQueries

DATASET = Dataset("raw")
SCHEMAS = ["base", "rules"]

ASSERTED = rdflib.Graph()     
GRAPH = rdflib.Graph()        
ERRORS = Counter()

TITLE = LEVEL = CREDIT = SCHOOL = STUDY_TYPE = {}


# =========================
# App entry
# =========================

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend")

def load():
    global ASSERTED, GRAPH, ERRORS, TITLE, LEVEL, CREDIT, SCHOOL, STUDY_TYPE
    world, _, _ = utils.load_everything(DATASET, SCHEMAS)
    ASSERTED = queries.to_graph(world)
    utils.run_reasoner(world)
    GRAPH = queries.to_graph(world)
    _, ERRORS, _ = shapes.check(world)

    TITLE = column("hasTitle")
    LEVEL = column("hasLevel")
    CREDIT = column("hasCredit")
    SCHOOL = column("belongsTo")
    STUDY_TYPE = column("hasStudyType")
    
# =========================
# BINDING HELPERS
# =========================
def uni(name):
    """Schema term, e.g. uni("Unit"), uni("hasLevel")"""
    return URIRef(config.SCHEMA_IRI + name)


def data(name):
    """Data individual, e.g. data("CITS3005")"""
    return URIRef(DATASET.iri + name)


def run(sparql, graph=None, **bindings):
    if graph is None:
        graph = GRAPH      
    return queries.run(graph, DATASET, sparql, **bindings)

def column(prop):
    """entity -> value for one property, e.g. column("hasLevel")["CITS3005"] -> "3" """
    return dict(run(Q.query_by_relation(), selectedRelation=uni(prop)))


def facts(name, graph=None):
    """Every property of one entity: {"hasUnit": [...], "hasTitle": [...], ...}"""
    result = defaultdict(list)
    for prop, value in run(Q.get_properties(), graph, selectedEntity=data(name)):
        result[prop].append(value)
    return result

def first(values):
    return values[0] if values else ""

TITLE = column("hasTitle")
LEVEL = column("hasLevel")
CREDIT = column("hasCredit")
SCHOOL = column("belongsTo")
STUDY_TYPE = column("hasStudyType")


def listing(class_name):
    """All entities of a class as (name, code, title) rows."""
    return run(Q.list_by_entity_type(), selectedType=uni(class_name))


def unit_row(name):
    return {"code": name, "title": TITLE.get(name, ""),
            "level": LEVEL.get(name, ""), "credit": CREDIT.get(name, "")}


def major_row(name):
    return {"code": name, "title": TITLE.get(name, ""), "school": SCHOOL.get(name, "")}


def table(title, columns, rows):
    return render_template("results.html", title=title, columns=columns, rows=rows)

def binding(value):
    if value.startswith("uni:"):
        return uni(value[4:])
    if value.startswith("data:"):
        return data(value[5:])
    if value.isdigit():
        return Literal(int(value))
    return Literal(value)

# =========================
# PAGES
# =========================
@app.route("/")
def home():
    return render_template("home.html", built=DATASET.is_built())

@app.route("/rebuild", methods=["POST"])
def rebuild():
    pipeline.build()
    load()
    return redirect(url_for("home"))


@app.route("/run/<name>")
def run_query(name):
    method = getattr(Q, name, None)
    if name.startswith("_") or not callable(method):
        abort(404)
    sparql = method()
    bindings = {key: binding(value) for key, value in request.args.items()}
    return table(name, queries.headers(DATASET, sparql), run(sparql, **bindings))

@app.route("/degrees")
def degrees():
    rows = [{"code": code, "title": title, "study_type": STUDY_TYPE.get(name, "")}
            for name, code, title in listing("Degree") if title]
    return render_template("lists/degrees.html", degrees=rows)


@app.route("/majors")
def majors():
    rows = [major_row(name) for name, code, title in listing("Major")]
    return render_template("lists/majors.html", majors=rows)


@app.route("/units")
def units():
    rows = [unit_row(name) for name, code, title in listing("Unit") if title]
    return render_template("lists/units.html", units=rows)


@app.route("/degree/<code>")
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


@app.route("/major/<code>")
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


@app.route("/unit/<code>")
def unit_details(code):
    f = facts(code)
    if not f:
        abort(404)
    direct = facts(code, ASSERTED)["hasPrerequisite"]     # asserted (from data)
    every = f["hasPrerequisite"]                           # inferred (transitive)
    unit = unit_row(code)
    unit["direct_prereqs"] = [unit_row(p) for p in sorted(set(direct))]
    unit["all_prereqs"] = [unit_row(p) for p in sorted(set(every))]
    return render_template("details/unit.html", unit=unit)


# =========================
# QUERIES
# =========================
@app.route("/queries")
def queries_page():
    return render_template("queries.html")


@app.route("/query/foundational")
def foundational_query():
    return table("Foundational units by degree", ["Degree", "Unit"],
                 run(Q.foundational_units()))


@app.route("/query/average-majors")
def average_query():
    return table("Average majors by degree type", ["Degree type", "Average majors"],
                 run(Q.average_majors()))


@app.route("/query/location")
def location_query():
    name = request.args.get("location", "")
    rows = run(Q.majors_in_location(), selectedLocation=data("Location_" + utils.slug(name)))
    return table(f"Majors available in {name}", ["Code", "Title"], rows)


@app.route("/search")
def search():
    q = request.args.get("q", "").strip()
    rows = run(Q.outcome_search(), searchTerm=Literal(q)) if q else []
    return table(f'Majors matching "{q}"', ["Code", "Title", "Matching outcome"], rows)


@app.route("/validation")
def validation():
    return table("Data validation", ["Problem", "Count"], sorted(ERRORS.items()))


if DATASET.is_built():
    load()
    
if __name__ == "__main__":
    # Apparently port 5000 is taken on Mac so using 5001
    app.run(debug=True, use_reloader=False, threaded=False, port=5001)