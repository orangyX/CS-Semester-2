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

    class OutCome(Thing):
        pass

    # And the properties
    class hasPrerequisite(ObjectProperty): # ObjectProperty; links an instance to another instance
        domain = [Unit] # Unit requiring the prerequisite
        range = [Unit] # Required unit

    class isPrerequisiteOf(ObjectProperty):
        domain = [Unit]
        range = [Unit]
        inverse_property = hasPrerequisite # Declare inverse property

    class hasCreditPrerequisite(DataProperty, FunctionalProperty): # FunctionalProperty -> link to a single entity
        domain = [Unit]
        range = [int] # Number of credits required to be eligible to take the unit (likely a multiple of 6)

    class inMajor(ObjectProperty):
        domain = [Unit]
        range = [Major]

    class inDegree(ObjectProperty):
        domain = [Major]
        range = [Degree]

    class creditsAcquirable(DataProperty, FunctionalProperty):
        domain = [Unit]
        range = [int] # The number of credits acquired from passing the unit (6)

    class locatedIn(ObjectProperty):
        domain = [Unit]
        range = [Location]

    class hasOutCome(ObjectProperty):
        domain = [Unit]
        range = [OutCome]

    class unitLevel(DataProperty):
        domain = [Unit]
        range = [int] # Validation; level >= 1

if __name__ == "__main__":
    # Add more here

    onto.save(file="university_ot.owl", format="rdfxml")