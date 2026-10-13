from owlready2 import * 
from university_ot import OntologySchema # The schema load

w = World()
onto = w.get_ontology()

ontology = OntologySchema(w, onto)