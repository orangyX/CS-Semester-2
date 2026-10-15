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
            
            # Any degree is also a BHPhil
            class BachelorOfPhilosophy(b.Degree):
                equivalent_to = [b.Degree & b.hasTitle.value("Bachelor of Philosophy (Honours)")]

            # Transitive property
            # A degree offers any unit available to a major the degree owns
            class offersUnit(b.Degree >> b.Unit, ObjectProperty):
                pass
            offersUnit.property_chain.append(PropertyChain([b.hasMajor, b.hasUnit]))

            # A major is dependent of ALL prerequisites of its units.
            # even outside the major
            class dependsOnUnit(b.Major >> b.Unit, ObjectProperty):
                pass
            dependsOnUnit.property_chain.append(PropertyChain([b.hasUnit, b.hasPrerequisite]))

            # This just makes sure mapped values are correct.
            # Create classes
            class FirstYearUnit(b.Unit):
                equivalent_to = [b.Unit & b.hasLevel.value(1)]

            class SecondYearUnit(b.Unit):
                equivalent_to = [b.Unit & b.hasLevel.value(2)]

            class ThirdYearUnit(b.Unit):
                equivalent_to = [b.Unit & b.hasLevel.value(3)]

            # Any unit that is above level 3 is considered a post grad unit.
            class PostgradUnit(b.Unit):
                equivalent_to = [b.Unit & b.hasLevel.some(ConstrainedDatatype(int, min_inclusive=4))]
            Imp().set_as_rule(
                'hasMajor(?d, ?m), hasStudyType(?d, ?t), Bachelor(?t), '
                'hasTitle(?p, "Bachelor of Philosophy (Honours)") -> hasMajor(?p, ?m)',
                namespaces=ns,
            )
            
            # An outcome of a core unit is an outcome of it's major.
            Imp().set_as_rule(
                'hasUnit(?m, ?u), hasOutcome(?u, ?o) -> hasOutcome(?m, ?o)',
                namespaces=ns,
            )
            
            
            

            
            b.hasMajor.property_chain.append(PropertyChain([b.includesDegree, b.hasMajor]))

        return self.onto