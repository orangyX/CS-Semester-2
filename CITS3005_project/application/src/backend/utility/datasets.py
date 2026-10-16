"""

###########
DONT WORRY ABOUT THIS FILE
##########
datasets.py - everything to do with dataset and schema files.

This will handle when a new data set or schema is loaded into the application

This allows the user to upload a made schema or a dataset to be made into a graph

This means there can be different rule sets 

Fixed settings (IRIs, root folders) come from config.py.

A note is while this will accept a dataset, a schema thats not compatible will return
a fucked up graph

Update this was reduced in scope to handle pathing of data and outputs 
and avoiding basic clashing.
"""

import re
from pathlib import Path

import utility.config as config

# Basic regular expression to control 
VALID_NAME = re.compile(r"^[A-Za-z0-9_-]+$")


def check_name(name: str) -> str:
    if not VALID_NAME.match(name):
        raise ValueError(f"Invalid name: {name!r}")
    return name

class Dataset:
    def __init__(self, name: str):
        self.name = check_name(name)

    # =======================
    # Property objects, this allows objects to be made and checked for correctness
    
    @property
    def data_dir(self) -> Path:
        return config.DATASETS_DIR / self.name

    @property
    def graph_file(self) -> Path:
        return config.GRAPHS_DIR / f"{self.name}.owl"
    
    @property
    def iri(self) -> str:
        return f"{config.DATA_IRI_BASE}{self.name}#"    # namespace for its entities
    
    def is_built(self) -> bool:
        return self.graph_file.exists()
    
def schema_path(name: str) -> Path:
    return config.SCHEMAS_DIR / f"{check_name(name)}.owl"

