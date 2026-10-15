"""
rules2.py - rules on top of the base2 schema.

Loads the saved base schema, creates its own ontology that imports it,
and adds the spec's inference rules. 

Checks (self-prerequisites,
missing majors, credit limits) live in SHACL, not here.
"""

from owlready2 import *

from utility import utils


class Rules:
    def __init__(self, iri: str, base_name: str, include_outcomes: bool = True):
        self.include_outcomes = include_outcomes
        self.world = World()
        self.base = utils.load_schema(self.world, base_name)
        self.onto = self.world.get_ontology(iri)
        self.onto.imported_ontologies.append(self.base)
        self.build()

    def save(self, name: str):
        return utils.save_schema_onto(self.onto, name)

    def build(self):
        b = self.base                
        ns = [b, self.onto]          

        with self.onto:            
            
            b.Degree.is_a.append(b.hasMajor.some(b.Major))
            
            class BachelorOfPhilosophy(b.Degree):
                equivalent_to = [b.Degree & b.hasTitle.value("Bachelor of Philosophy (Honours)")]

            Imp().set_as_rule(
                'hasMajor(?d, ?m), hasStudyType(?d, ?t), Bachelor(?t), '
                'hasTitle(?p, "Bachelor of Philosophy (Honours)") -> hasMajor(?p, ?m)',
                namespaces=ns,
            )
            
            b.hasMajor.property_chain.append(PropertyChain([b.includesDegree, b.hasMajor]))

        return self.onto