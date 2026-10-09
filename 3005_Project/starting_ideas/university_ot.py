from owlready2 import *

w = World() # Let w be a fresh world
onto = w.get_ontology("http://uwa/uni.ot#") # IRI 

with onto:
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

    class degreeCode(Degree >> str, DataProperty, FunctionalProperty): pass

    class degreeTitle(Degree >> str, DataProperty, FunctionalProperty): pass

    class degreeSchool(Degree >> School, ObjectProperty): pass

    class degreeCreditsToComplete(Degree >> int, DataProperty, FunctionalProperty): pass

    class degreeFullTimeDuration(Degree >> int, DataProperty, FunctionalProperty): pass

    class degreeLocation(Degree >> Location, ObjectProperty): pass

    class degreeMajors(Degree >> Major, ObjectProperty): pass

    # MAJOR SPECIFIC PROPERTIES ---------------------------------------------------------
    class majorCode(Major >> str, DataProperty, FunctionalProperty): pass

    class majorTitle(Major >> str, DataProperty, FunctionalProperty): pass

    class majorSchool(Major >> School, ObjectProperty): pass

    class majorDescription(Major >> str, DataProperty): pass

    class majorOutcomes(Major >> str, DataProperty): pass

    # UNIT SPECIFIC PROPERTIES ----------------------------------------------------------
    class Assessment(Thing): pass # Stores assessment modes, such as exam, research, etc.

    class unitCode(Unit >> str, DataProperty, FunctionalProperty): pass

    class unitTitle(Unit >> str, DataProperty, FunctionalProperty): pass

    class unitSchool(Unit >> School, ObjectProperty): pass

    class unitLevel(Unit >> int, DataProperty, FunctionalProperty): pass

    class unitDescription(Unit >> str, DataProperty): pass

    class unitAwardsCredits(Unit >> int, DataProperty, FunctionalProperty): pass

    class unitSemesterAvailability(Unit >> int, DataProperty): pass

    class unitOfferedAtLocation(Unit >> Location, ObjectProperty): pass

    class unitModes(Unit >> str, DataProperty): pass

    class unitPartOfMajor(Unit >> Major, ObjectProperty): pass

    class unitOutcomes(Unit >> str, DataProperty): pass

    class unitAssessmentTypes(Unit >> Assessment, ObjectProperty): pass

    class unitWeeklyContactHours(Unit >> int, DataProperty, FunctionalProperty): pass

    # DEFINE RELATIONS HERE -------------------------------------------------------------

    # PREREQUISITE RESTRICTIONS
if __name__ == "__main__":
    # Add more here

    onto.save(file="university_ot.owl", format="rdfxml")