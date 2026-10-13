from owlready2 import * 
from university_ot import OntologySchema # The schema load
import json
from config import DEGREES_JSON, BASE_IRI, SCHEMA_FILE, INFER_PROPERTY_VALUES, REASONER, INFER_DATA_PROPERTY_VALUES

def build_graph():
    w = World()
    onto = w.get_ontology(BASE_IRI)

    ontology = OntologySchema(w, onto)
    data = json.loads(DEGREES_JSON.read_text(encoding="utf-8"))

    with onto:
        for code, entry in data.items():
            degree = onto.Degree(code)
    onto.save(file="university_ot.owl", format="rdfxml")
    run_reasoner(w)


def run_reasoner(world):
    if REASONER == "pellet":
        sync_reasoner_pellet(world,
                             infer_property_values=INFER_PROPERTY_VALUES,
                             infer_data_property_values=INFER_DATA_PROPERTY_VALUES)
    elif REASONER == "hermit":
        sync_reasoner_hermit(world, infer_property_values=INFER_PROPERTY_VALUES)

build_graph()