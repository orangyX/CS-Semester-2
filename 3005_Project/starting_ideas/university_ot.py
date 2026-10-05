from owlready2 import *

w = World()
onto = w.get_ontology("http://uwa/uni.ot#")

with onto:
    # These shall be the classes
    class Degree(Thing):
        pass

    class Major(Thing):
        pass

    class Unit(Thing):
        pass

    # And the properties
    class hasPrerequisite(ObjectProperty): # ObjectProperty; links an instance to another instance
        domain = [Unit] # Unit requiring the prerequisite
        range = [Unit] # Required unit

    class isPrerequisiteOf(ObjectProperty):
        domain = [Unit]
        range = [Unit]
        inverse_property = hasPrerequisite # Declare inverse property

    class hasCreditPrerequisite(ObjectProperty):
        # This one will error; a unit has exactly one credit prereq; 0 credits, or more than 0
        # The required credits shall be an integer
        domain = [Unit]
        range = [int]
        # TO DO
        pass

    class inMajor(ObjectProperty):
        domain = [Unit]
        range = [Major]
        # TO DO
        pass

    class inDegree(ObjectProperty):
        domain = [Major]
        range = [Degree]
        # TO DO
        pass