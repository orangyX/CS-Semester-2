"""
rules2.py - rules on top of the base2 schema.

Loads the saved base schema, creates its own ontology that imports it,
and adds the spec's inference rules. 

Checks (self-prerequisites,
missing majors, credit limits) live in SHACL, not here.

Update: moved to used rule set. 
Also one these damn rules is taking forever.
"""

from owlready2 import *

from utility import utils


class Rules:
    def __init__(self, iri: str, base_name: str, include_outcomes: bool = True):
        self.include_outcomes = include_outcomes
        self.world = World()
        self.base = utils.load_schema(self.world, base_name) # Get owl schema
        self.onto = self.world.get_ontology(iri)             # Give namespace
        self.onto.imported_ontologies.append(self.base)      # Save rules onto schema 
        self.build()

    def save(self, name: str):
        return utils.save_schema_onto(self.onto, name)

    def build(self):
        b = self.base           # schema terms         
        ns = [b, self.onto]     # Namespace

        with self.onto:            
            
            # A degree must have atleast one major
            # Uses restriction method, ALL Degrees has relation 'hasMajor' to some major
            # We don't force this ruling but catch in shacl as its openworld assumption
            # Most errors will come from 'prerequisite courses' where the degree isnt listed in degrees
            b.Degree.is_a.append(b.hasMajor.some(b.Major))
            
            # A major of a degree is also a major of a combined degree where that degree is included
            # If b included degree and degree hasMajor m. then combined degree has m
            b.hasMajor.property_chain.append(PropertyChain([b.includesDegree, b.hasMajor]))
        
            # Add the bachelor of philosophy as a class, identify through name
            class BachelorOfPhilosophy(b.Degree):
                equivalent_to = [b.Degree & b.hasTitle.value("Bachelor of Philosophy (Honours)")]

            # Any major of another bachelor degree is a major of BHPhil
            # if d hasMajor m AND d hasStudyType t AND t is a bachelor
            # -> essentially if d is a bachelor and has a major
            # and philosophy entity has correct name, then m is also a major of p
            Imp().set_as_rule(
                'hasMajor(?d, ?m), hasStudyType(?d, ?t), Bachelor(?t), '
                'hasTitle(?p, "Bachelor of Philosophy (Honours)") -> hasMajor(?p, ?m)',
                namespaces=ns,
            )
            
            # Transitive property
            # A degree offers any unit available to a major the degree owns
            class offersUnit(b.Degree >> b.Unit, ObjectProperty):
                pass
            offersUnit.property_chain.append(PropertyChain([b.hasMajor, b.hasUnit]))

            # Transitive property
            # If a major has a unit u AND u hasPrerequisite pr then major depends on that unit
            # Major depends on any chain of unit prerequisites even outside its inital unit relation.
            class dependsOnUnit(b.Major >> b.Unit, ObjectProperty):
                pass
            dependsOnUnit.property_chain.append(PropertyChain([b.hasUnit, b.hasPrerequisite]))

            # Create inferred classes.
            # Convert level literals to new class type which can be queried
            class FirstYearUnit(b.Unit):
                equivalent_to = [b.Unit & b.hasLevel.value(1)]

            class SecondYearUnit(b.Unit):
                equivalent_to = [b.Unit & b.hasLevel.value(2)]

            class ThirdYearUnit(b.Unit):
                equivalent_to = [b.Unit & b.hasLevel.value(3)]

            # Any unit that is above level 3 is considered a post grad unit.
            class PostgradUnit(b.Unit):
                equivalent_to = [b.Unit & b.hasLevel.some(ConstrainedDatatype(int, min_inclusive=4))]
            

            
            # This is abit dodgy, when building we kinda had the assumption that the
            # units were units available to that major not nessessarliy core units. 
            
            # An outcome of a core unit is an outcome of it's major.
            # 
            # Imp().set_as_rule(
            #     'hasUnit(?m, ?u), hasOutcome(?u, ?o) -> hasOutcome(?m, ?o)',
            #     namespaces=ns,
            # )
            
            # Change, ASSUME if its directly under major its a core unit of the major.
            
            # Unit under m is a core unit of m
            class hasCoreUnit(b.Major >> b.Unit, ObjectProperty):
                pass
            b.hasUnit.is_a.append(hasCoreUnit)     

            # inverse of hasCoreUnit
            class coreUnitOf(b.Unit >> b.Major, ObjectProperty):
                inverse_property = hasCoreUnit

            # core unit c is in atleast 1 major
            class CoreUnit(b.Unit):
                equivalent_to = [b.Unit & coreUnitOf.some(b.Major)]
                
            # An outcome of a core unit is an outcome of it's major.
            Imp().set_as_rule(
                'hasCoreUnit(?m, ?u), hasOutcome(?u, ?o) -> hasOutcome(?m, ?o)',
                namespaces=ns,
            )
        return self.onto