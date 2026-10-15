"""
We want to be able to build a knowledge graph from the data supplied

The builder will own its own world
It's able to load 
    a schema as a .owl by name from (data/schema)
    a dataset as its own JSON file set and IRI
    
It will then create entites with the provided ontology

Should save out to data/graphs/<dataset>.owl.

We can have multiple graphs and swap between them

Inputs MUST be passed in explicitly

Note we also have an expectation currently for parsing data which should be generalised 
to a similar format as given dict{dict{key,  value}} set. This will be the expectation.

"""
import json
from pathlib import Path

from owlready2 import * 

import backend.utility.config as config 
from datasets import Dataset, schema_path



class KnowledgeGraphBuilder:
    """
    This class owns build fucntions and will own the world
    The ontology schema provided and the data from the json files.
    We can modulate from here by having a nested dict for each name
    Space we wish to process.
    """
    def __init__(self):
        self.world = World()
        self.onto = None        # The ontology schema provided
        self.data_onto = None   # data ontology (entities), in the dataset's namespace
        self.dataset = None     # the Dataset being used
        self.data = {}          # loaded JSON file
        
    
    # =========================
    # LOADING AND SAVING OF FILES
    # Allows us to load different schemas and datasets
    # =========================
    def load_schema(self, path=config.SCHEMA_TEST_FILE):
        """
        Takes a path from a schema file and loads it as an ontology.
        """
        self.onto = self.world.get_ontology(Path(path).as_uri()).load()
        return self.onto
    
    def load_dataset(self, data_dir=config.DATA_DIR):
        """
        Get a set of data, this gets every json inside a specified file
        """
        for path in sorted(Path(data_dir).glob("*.json")):
            with path.open(encoding="utf-8") as f:
                self.data[path.stem] = json.load(f)
        return self.data
    
    def save(self, path=config.DATA_TEST_FILE):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.onto.save(file=str(path), format="rdfxml")
        
    def run_reasoner(self):
        if config.REASONER == "pellet":
            sync_reasoner_pellet(self.world,
                                infer_property_values=config.INFER_PROPERTY_VALUES,
                                infer_data_property_values=config.INFER_DATA_PROPERTY_VALUES)
        elif config.REASONER == "hermit":
            sync_reasoner_hermit(self.world, infer_property_values=config.INFER_PROPERTY_VALUES)

    # =========================
    # This section holds functions that build the actual graph
    # =========================
    def build_graph(self):
        with self.onto:
            self._create_entities()
            self._link_entities()

    def _create_entities():
        pass
    
    def _link_entites():
        pass
    
