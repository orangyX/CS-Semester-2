"""
Basic shared structure and expected minimal ontology
"""

from owlready2 import *
 
import backend.utility.config as config
from utility import utils
 

class OntologyBase:
    """
    Maintain a set base ontology, this should always
    exist includes basic facts about the graph
    such that extensions can be added for different rule sets 
    
    Will validate the base so its continuous and at MINIMUM 
    the graph works.
    
    This is mostly take from your stuff but should be overarching strucuture
    And can explore options in Basic formatting.
    """
    def __init__(self, iri: str):
        self.world = World()                       # own world, isolated from any data
        self.onto = self.world.get_ontology(iri)
        self.build()

    def save(self, name: str):
        return utils.save_schema_onto(self.onto, name)

    def build(self):
        with self.onto:
            
            # Most basic attributes.
            # Potentially make 
            # Enrollable -> degree/Major/ Unit
            # Abstract out shared information here.
            # code / name / school
            
            class Enrollable(Thing):
                pass

            class Degree(Enrollable):
                pass

            class Major(Enrollable):
                pass

            class Unit(Enrollable):
                pass
            
            class Location(Thing):
                pass
 
            # DEGREE SPECIFIC PROPERTIES --------------------------------------------------------
            # Items that will certainly be reused several times will be classes
            class School(Thing): pass # Stores the schools themselves
 
            class StudyType(Thing): pass # Stores Bachelors, Masters, PhD, etc.
 
            class Bachelor(StudyType): pass
 
            class Honours(StudyType): pass
 
            class CombinedBachelor(StudyType): pass
 
            class Masters(StudyType): pass
 
            class PhD(StudyType): pass
 
            class degreeCode(Degree >> str, DataProperty, FunctionalProperty): pass
 
            class degreeTitle(Degree >> str, DataProperty, FunctionalProperty): pass
 
            class degreeSchool(Degree >> School, ObjectProperty): pass
 
            class degreeCreditsToComplete(Degree >> int, DataProperty, FunctionalProperty): pass
 
            class degreeFullTimeDuration(Degree >> int, DataProperty, FunctionalProperty): pass
 
            class degreeLocation(Degree >> Location, ObjectProperty): pass
 
            # Added after
            class degreeStudyType(Degree >> StudyType, ObjectProperty, FunctionalProperty): pass
 
            class combinedDegreeIncludes(Degree >> Degree, ObjectProperty, IrreflexiveProperty): pass
 
            # MAJOR SPECIFIC PROPERTIES ---------------------------------------------------------
            class majorCode(Major >> str, DataProperty, FunctionalProperty): pass
 
            class majorTitle(Major >> str, DataProperty, FunctionalProperty): pass
 
            class majorSchool(Major >> School, ObjectProperty): pass
 
            class majorDescription(Major >> str, DataProperty): pass
 
            class majorOutcomes(Major >> str, DataProperty): pass
 
            class majorBridgingUnits(Major >> Unit, ObjectProperty): pass
 
            # Added after
            class majorProgression(Major >> int, DataProperty): pass # Stores major level
 
            class majorCreditsAtLevel(Major >> int, DataProperty): pass # Stores the number of credits per major-level
 
            # UNIT SPECIFIC PROPERTIES ----------------------------------------------------------
            class ContactMode(Thing): pass
 
            class contactModeHours(ContactMode >> int, DataProperty, FunctionalProperty): pass
 
            class contactModeType(ContactMode >> str, DataProperty, FunctionalProperty): pass
 
            class unitCode(Unit >> str, DataProperty, FunctionalProperty): pass
 
            class unitTitle(Unit >> str, DataProperty, FunctionalProperty): pass
 
            class unitSchool(Unit >> School, ObjectProperty): pass
 
            class unitLevel(Unit >> int, DataProperty, FunctionalProperty): pass
 
            class unitDescription(Unit >> str, DataProperty, FunctionalProperty): pass
 
            class unitAwardsCredits(Unit >> int, DataProperty, FunctionalProperty): pass
 
            class unitSemesterAvailability(Unit >> str, DataProperty): pass
 
            class unitLocation(Unit >> Location, ObjectProperty): pass
 
            class unitModes(Unit >> str, DataProperty): pass
 
            class unitPartOfMajor(Unit >> Major, ObjectProperty): pass # This is ambiguous; we need to answer the question "a unit is core in a major"
 
            class unitOutcomes(Unit >> str, DataProperty): pass
 
            class unitAssessmentTypes(Unit >> str, DataProperty): pass
 
            class unitContactTypes(Unit >> ContactMode, ObjectProperty): pass
 
            # UNIT RELATIONS --------------------------------------------------------------------
            class unitHasPrerequisite(Unit >> Unit, ObjectProperty, TransitiveProperty): pass # Owl complains if something is transitive and irreflexive; this rule needs to be enforced elsehwere
 
            class unitIsPrerequisiteOf(Unit >> Unit, ObjectProperty):
                inverse_property = unitHasPrerequisite # Set it once, then it also applies to the other
 
            class unitIsCoreInMajor(Unit >> Major, ObjectProperty): pass # OWA; non-added info is unkown
 
            # MAJOR RELATIONS -------------------------------------------------------------------
            class majorHasCoreUnit(Major >> Unit, ObjectProperty):
                inverse_property = unitIsCoreInMajor
 
            class majorInDegree(Major >> Degree, ObjectProperty): pass
 
            # DEGREE RELATIONS ------------------------------------------------------------------
            class degreeHasMajor(Degree >> Major, ObjectProperty): # Each deg. has at least one major
                inverse_property = majorInDegree
 
            # STUDY-TYPE INDIVIDUALS ------------------------------------------------------------
            # Shared vocabulary: the parser links each degree to one of these
            bachelor = Bachelor("BP")
            honours = Honours("BH")
            combined = CombinedBachelor("CB")
 
        return self.onto
 
 
if __name__ == "__main__":
    # OPEN: switch to config.SCHEMA_IRI and "base" once this is the final schema
    path = OntologyBase(config.TEST_IRI).save("test_base")
    print(f"Base schema saved to {path}")
 