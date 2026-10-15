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


def table(title, columns, rows):
    return render_template("results.html", title=title, columns=columns, rows=rows)

def run(sparql, graph=None, **bindings):
    if graph is None:
        graph = GRAPH      
    return queries.run(graph, DATASET, sparql, **bindings)

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
    pipeline.build()
    return redirect(url_for("/load"))

@app.route("/load", methods=["POST"])
def load():
    global ASSERTED, GRAPH, ERRORS, TITLE, LEVEL, CREDIT, SCHOOL, STUDY_TYPE
    world, _, _ = utils.load_everything(DATASET, SCHEMAS)
    ASSERTED = queries.to_graph(world)
    utils.run_reasoner(world)
    GRAPH = queries.to_graph(world)
    _, ERRORS, _ = shapes.check(world)
    return redirect(url_for("home"))
    

@app.route("/search")
def search():
    q = request.args.get("q", "").strip()
    rows = run(Q.outcome_search(), searchTerm=Literal(q)) if q else []
    return table(f'Majors matching "{q}"', ["Code", "Title", "Matching outcome"], rows)


@app.route("/query")
def query():
    pass


@app.route("/validation")
def validation():
    return table("Data validation", ["Problem", "Count"], sorted(ERRORS.items()))


# @app.route("/unit/<code>")

    
if __name__ == "__main__":
    # Apparently port 5000 is taken on Mac so using 5001
    app.run(debug=True, use_reloader=False, threaded=False, port=5001)