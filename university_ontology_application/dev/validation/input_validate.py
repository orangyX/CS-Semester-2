from pyshacl import validate
from rdflib import Graph
from pathlib import Path
from application.src.backend.university_ot import w, onto
from shacl_rules import degree_sh, major_sh, unit_sh

class ShaclValidation:
    def __init__(self):
        # The rules (i.e., shapes) which shall provide constraints for the ontology
        self.degree_rules = None
        self.major_rules = None
        self.unit_rules = None

        # The graphs, storing the ontology data, and shapes
        self.ont_graph = Graph()
        self.sh_graph = Graph()
        pass

    def load_shapes(self):
        self.degree_rules = degree_sh
        self.major_rules = major_sh
        self.unit_rules = unit_sh

    def load_ot_graph(self):
        ont_data = w.as_rdflib_graph()

        for s, p, o in ont_data:
            self.ont_graph.add((s, p, o))

        self.sh_graph.parse(data=degree_sh, format="turtle")
