from owlready2 import *

class OntologySchema:

    def __init__(self, world: World, ontology: Ontology, file, format):
        self.w = world
        self.onto = ontology

        self.build_schema()
        self.save(file, format)

    def build_schema(self):
        with self.onto:
            # Base and most abstracted attributes
            class Degree(Thing):
                pass

            class Major(Thing):
                pass

            class Unit(Thing):
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

            class combinedBachelorIncludes(Degree >> Degree, ObjectProperty, IrreflexiveProperty): pass

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

            class FloatingUnit(Unit): pass # Units in prerequisite units which are not included in the units json file

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

            # PRE-INSTANTIATED INDIVUDLALS, REQUIRED FOR SWRL RULINGS ---------------------------
            bachelor = Bachelor("Bachelorscourse")
            honour = Honours("Honourscourses")
            combined_bachelor = CombinedBachelor("Combinedbachelorscourses")

            bachelor_philosophy = Degree("BH005")

            # SWRL CONSTRAINTS ------------------------------------------------------------------

            # An outcome of a core unit is an outcome of a major
            unit_major_outcome_rule = Imp().set_as_rule(
                "unitIsCoreInMajor(?u, ?m), unitOutcomes(?u, ?o) -> majorOutcomes(?m, ?o)"
            ) # A unit core in a major with outcomes implies that that major also has the outcomes of the unit

            # Any major of another bachelor's degree is a major in the bachelor of philosophy
            philosophy_major_rule = Imp().set_as_rule(
                "degreeHasMajor(?d, ?m), StudyType"
            )
            # TESTING - DELETE THIS PRIOR TO SUBMISSION -----------------------------------------
    def save(self, f, fo):
        self.onto.save(file=f, format=fo)