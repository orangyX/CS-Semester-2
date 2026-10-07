from owlready2 import *

w = World() # Let w be a fresh world
onto = w.get_ontology("http://uwa/uni.ot#") # IRI 

with onto:
    # These shall be the classes
    class Degree(Thing):
        pass

    class Major(Thing):
        pass

    class Unit(Thing):
        pass

    class Location(Thing):
        pass

    class Outcome(Thing):
        pass

    # And the properties
    class hasPrerequisite(Unit >> Unit, IrreflexiveProperty, TransitiveProperty): # Because a unit cannot be its own prerequisite
        pass

    class isPrerequisiteOf(Unit >> Unit, IrreflexiveProperty, TransitiveProperty): # For the same reason, a unit cannot be a prerequisite of itself
        inverse_property = hasPrerequisite # Declare inverse property

    class hasCreditPrerequisite(Unit >> int, FunctionalProperty): # FunctionalProperty -> link to a single entity
        pass

    class unitInMajor(Unit >> Major):
        # Unit does not necessarily have to be part of a major
        pass

    class majorHasUnit(Major >> Unit):
        inverse_property = unitInMajor

    class majorInDegree(Major >> Degree):
        # Each degree is comprised of at least one major
        pass

    class degreeHasMajor(Degree >> Major):
        inverse_property = majorInDegree

    class creditsAcquirable(Unit >> int, FunctionalProperty):
        pass

    class locatedIn(Unit >> Location):
        pass

    class hasOutcome(Unit >> Outcome):
        pass

    class unitLevel(Unit >> int, FunctionalProperty):
        pass

    # PREREQUISITE RESTRICTIONS

    # CREDIT PREREQUISITE RESTRICTIONS

    # UNIT IN MAJOR + MAJOR HAS UNIT RESTRICTIONS
    Unit.is_a.append(unitInMajor.some(Major)) # FIX; because a unit does not necessarily need to be part of a major
    Major.is_a.append(majorHasUnit.some(Unit)) # A major is comprised of at least one unit

    # DEGREE/MAJOR RESTRICTIONS
    Degree.is_a.append(degreeHasMajor.some(Major)) # Anything with a major is a degree; necessary condition
    Major.is_a.append(majorInDegree.some(Degree)) # Anything in a degree is a major

    # CORE UNIT; DECIDING ON WHAT MAKES A UNIT A CORE

if __name__ == "__main__":
    # Add more here

    onto.save(file="university_ot.owl", format="rdfxml")