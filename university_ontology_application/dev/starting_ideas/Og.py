"""
Note masters typing '73457'
OUT OF SCOPE
Currently, we will ignore faults in the factual data and first begin
with relational sets (No string manipulation)

Comment notes:
Decision: What i chose
Options: Other consideration to explore if you need the change
Why: Just reason to ideas
Status: Just define if this is an open or closed decision.
fd 
-e
PROPERTY TYPES
Object property (ObjectProperty): links 2 instances
Data property (DataProperty): link an instance to literal propery
Annotation property (AnnotationProperty): Link instance to META data for human use but not graph information

Functional	        At most one value per subject
Inverse functional	A value identifies a unique subject (key-like)
Transitive	        A→B and B→C gives A→C
Symmetric	        A→B gives B→A
Asymmetric	        A→B means never B→A
Reflexive	        Everything relates to itself
Irreflexive	        Nothing relates to itself

Think of query as set opertations:              Owl Function mapping
Union: In A or B (or both)                      : Or
Intersection: In A and B	                    : And
Difference: In A but not B	                    : A And Not B
Complement: Everything not in A	                : Not   # This assumes closed world cant prove againts open world
Symmetric difference: In exactly one, not both  
Subset: everything in A is also in B.           : is_a
Disjoint: A and B share nothing.                : AllDisjoint
Membership a single element belongs to the set
Empty set: the set with nothing in it.

Limits
Dont extend past level 4 units 
contact assumptions (weekly)
"""

# =========================
# IMPORTS
# =========================
# Ontology setup files
from owlready2 import *
import owlready2
from pathlib import Path

# Shacl imports  # iclude rdflib if file moves
from pyshacl import validate
# =========================
# DEFINITIONS / NAME SPACES
# We can use 2 namespace within this file for seperation between data instances
# And rulesets -> helps manage file seperation later and can import each other
# =========================
SCHEMA_IRI = "http://uwa/uni.ot#"      # classes, properties, restrictions, rules # Hold ontology facts
DATA_IRI   = "http://uwa/uni.data#"    # degrees, majors, units from the JSON # Hold the triples
BASE_DIR    = Path(__file__).resolve().parent
OUTPUT_DIR  = BASE_DIR / "output"
SCHEMA_FILE = OUTPUT_DIR / "university_ot.owl"   
DATA_FILE   = OUTPUT_DIR / "university_kg.owl" 

# =========================
# SETUP
# Items or classes that need to begin before building ontology
# =========================

w = World() # Let w be a fresh world
rule = w.get_ontology(SCHEMA_IRI)

# =========================
# SHAPES AND SHACL
# =========================




# =========================
# ONTOLOGIES
# =========================



# =========================
# FACTS
# =========================
with rule:
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

    rule.save(file="university_ot.owl", format="rdfxml")