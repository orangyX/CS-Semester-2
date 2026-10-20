"""
Basic shared structure and expected minimal ontology

NOTE we are adding the addition functions but they should be moved OUT
into an extension of the schema instead of directly 
"""

from owlready2 import *
 
import utility.config as config
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
        self.world = World()                     
        self.onto = self.world.get_ontology(iri)
        self.build()

    def save(self, name: str):
        return utils.save_schema_onto(self.onto, name)

    def build(self):
        with self.onto:
            
# --------------------------------------
            class Enrollable(Thing): pass
            class Degree(Enrollable): pass
            class Major(Enrollable): pass
            class Unit(Enrollable): pass

            # Make sure these are disjoint sets
            AllDisjoint([Degree, Major, Unit])
            
            # Prerequisite codes that aren't in the dataset
            class FloatingUnit(Unit): pass
# --------------------------------------  
            class School(Thing): pass
            class Location(Thing): pass
            
# --------------------------------------
            class StudyType(Thing): pass
            class Bachelor(StudyType): pass
            class Honours(StudyType): pass
            class Combined(StudyType): pass
# --------------------------------------
# Additional entities

            class ContactMode(Thing): pass     
# --------------------------------------

        
# --------------------------------------
# Handle relations   
            # SHARED
            class hasCode(Enrollable >> str, DataProperty, FunctionalProperty): pass
            class hasTitle(Enrollable >> str, DataProperty, FunctionalProperty): pass
            class belongsTo(Enrollable >> School, ObjectProperty, FunctionalProperty): pass
            class hasDescription(Enrollable >> str, DataProperty, FunctionalProperty): pass
            class hasOutcome(Enrollable >> str, DataProperty): pass
            class locatedIn(Enrollable >> Location, ObjectProperty): pass

            # DERGEES
            class hasStudyType(Degree >> StudyType, ObjectProperty, FunctionalProperty): pass
            class hasTotalPoints(Degree >> int, DataProperty, FunctionalProperty): pass
            class hasDuration(Degree >> int, DataProperty, FunctionalProperty): pass
            class hasMajor(Degree >> Major, ObjectProperty): pass
            class includesDegree(Degree >> Degree, ObjectProperty): pass
            class hasComponentTitle(Degree >> str, DataProperty): pass
            
            # MAJOR
            class hasUnit(Major >> Unit, ObjectProperty): pass
            class requiresBridging(Major >> Unit, ObjectProperty): pass
            class listedInDegree(Major >> Degree, ObjectProperty): pass   
            
            # UNITS
            class hasLevel(Unit >> int, DataProperty, FunctionalProperty): pass
            class hasCredit(Unit >> int, DataProperty, FunctionalProperty): pass
            class isAvailable(Unit >> bool, DataProperty, FunctionalProperty): pass
            class hasPrerequisite(Unit >> Unit, ObjectProperty, TransitiveProperty): pass
            class offeredIn(Unit >> str, DataProperty): pass
            class hasMode(Unit >> str, DataProperty): pass
            class hasAssessment(Unit >> str, DataProperty): pass
            class hasPrerequisiteText(Unit >> str, DataProperty, FunctionalProperty): pass

            class listedInMajor(Unit >> Major, ObjectProperty): pass      
            class hasMajorTitle(Unit >> str, DataProperty): pass         
            class requiresDegree(Unit >> Degree, ObjectProperty): pass    
            class hasAdvisedUnit(Unit >> Unit, ObjectProperty): pass
            class hasNote(Unit >> str, DataProperty, FunctionalProperty): pass
            class hasContact(Unit >> ContactMode, ObjectProperty): pass

            # Contact type information
            class contactType(ContactMode >> str, DataProperty, FunctionalProperty): pass
            class contactHours(ContactMode >> int, DataProperty, FunctionalProperty): pass
            # ===========================
            # INVERSES
            # ===========================
            class majorOf(Major >> Degree, ObjectProperty):
                inverse_property = hasMajor

            class unitOf(Unit >> Major, ObjectProperty):
                inverse_property = hasUnit

            class prerequisiteOf(Unit >> Unit, ObjectProperty):
                inverse_property = hasPrerequisite

        return self.onto
 

 