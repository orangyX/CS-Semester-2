"""
This is your rule set that you were adding to the function
"""


from owlready2 import *
 
import backend.utility.config as config
from utility import utils
 
 
class RulesSchema:
    def __init__(self, iri: str, base_name: str):
        self.world = World()
        self.base = utils.load_schema(self.world, base_name)
        self.onto = self.world.get_ontology(iri)
        self.onto.imported_ontologies.append(self.base)
        self.build()
 
    def save(self, name: str):
        return utils.save_schema_onto(self.onto, name)
 
    def build(self):
        ns = [self.base, self.onto]   # where rule names are looked up
 
        with self.onto:
            # PRE-INSTANTIATED INDIVIDUALS, REQUIRED FOR SWRL RULINGS -------------------------
            # Philosophy
            # DISCUSS: this BH005 is in the rules namespace, but the parser will create
            # BH005 in the dataset's namespace, so they'd be two different individuals.
            # Options: a BachelorOfPhilosophy class in base that the parser assigns,
            # or the parser reuses this individual.
            bPhil = self.base.Degree("BH005")
            bPhil.degreeStudyType = self.base.BH
 
            # SWRL CONSTRAINTS ------------------------------------------------------------------
 
            # An outcome of a core unit is an outcome of a major
            Imp().set_as_rule(
                "unitIsCoreInMajor(?u, ?m), unitOutcomes(?u, ?o) -> majorOutcomes(?m, ?o)",
                namespaces=ns,
            ) # A unit core in a major with outcomes implies that that major also has the outcomes of the unit
 
            # Any major of another bachelor's degree is a major in the bachelor of philosophy
            Imp().set_as_rule(
                "degreeHasMajor(?d, ?m), Bachelor(?b), degreeStudyType(?d, ?b) -> degreeHasMajor(BH005, ?m)",
                namespaces=ns,
            ) # Any degree with a major is a major in philosophy
 
            # # A major of degree X is also a major of any combined degree involving X
            # Imp().set_as_rule(
            #     "degreeHasMajor(?d, ?m), combinedDegreeIncludes(?c, ?d) -> degreeHasMajor(?c, ?m)",
            #     namespaces=ns,
            # ) # A degree with a major part of a combined degree means that the combined degree also has that major
 
            # A major must not exceed 48 credits at level 1
            # Imp().set_as_rule(
            #     # Stub for 13/10/2026
            # ) # Any major at level 1 cannot exceed 48 credits
 
        return self.onto
 
 
if __name__ == "__main__":
    # OPEN: switch names/IRIs once these are final
    path = RulesSchema("http://uwa/test.rules#", base_name="test_base").save("test_rules")
    print(f"Rules schema saved to {path}")