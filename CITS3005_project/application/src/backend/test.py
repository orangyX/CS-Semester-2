"""
This is a test schema

We can follow this later once established for final schema

"""

from owlready2 import *
from datasets import schema_path

class OntologySchema:
    """
    When we call this it creates its own world
    and builds its own ontology without any data
    only returns a schema that can be loaded
    
    Allows multiple schemas to be build and run 
    """
    def __init__(self, iri: str):
        self.world = World()
        self.onto = self.world.get_ontology(iri)
        self.build_schema()
        
    # Save the schema we build under any IRI
    def save(self, name: str):
        path = schema_path()    
        path.parent.mkdir(parents=True, exist_ok=True)
        self.onto.save(file=str(path), format="rdfxml")
        return path
    
    def build_schema(self):
        with self.onto:
            
            # ===========================
            # Describe entites here
            # ===========================
            class Degree(Thing): # Define a degree
                pass

            class Major(Thing): # Define a major
                pass
            
            # ==========================
            # Relation Rules
            # ==========================
            
            # ----- Degree <-> Major rule (Reflexive) -----
            class degreeHasMajor(ObjectProperty):
                domain = [Degree]
                range = [Major]
                
            class majorOfDegree(ObjectProperty):
                domain = [Major]
                range = [Degree]
                inverse_property = degreeHasMajor
        
        return self.onto