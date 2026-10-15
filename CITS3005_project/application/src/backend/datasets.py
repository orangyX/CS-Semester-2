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
"""

import re
from pathlib import Path

import utility.config as config

VALID_NAME = re.compile(r"^[A-Za-z0-9_-]+$")   # blocks names like "../x"


class ProtectedNameError(Exception):
    """Raise if a upload would overwrite a protected set."""

class Dataset:
    def __init__(self, name: str):
        if not VALID_NAME.match(name):
            raise ValueError(f"Invalid dataset name: {name!r}")
        self.name = name

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

    # =======================
    # Allow us to check if a dataset or schema already exists -> no point building a new one if one exists
    # Here we also make sure no protected data sets can be overwritten through upload
    
    @property
    def is_protected(self) -> bool:
        return self.name in config.PROTECTED_DATASETS

    def exists(self) -> bool:
        return self.data_dir.is_dir()

    def is_built(self) -> bool:
        return self.graph_file.is_file()

    def json_files(self) -> list[Path]:
        return sorted(self.data_dir.glob("*.json"))

    # ======================
    # Helper functions to create and save new datasets, we will simply return if a dataset already exists
    
    def create(self) -> "Dataset":
        """
        Create a folder if new or reuse if they exist
        """
        self.data_dir.mkdir(parents=True, exist_ok=True)
        config.GRAPHS_DIR.mkdir(parents=True, exist_ok=True)
        return self
    
    def _check_writable(self):
        if self.is_protected:
            raise ProtectedNameError(f"'{self.name}' is a default dataset and can't be changed")
 
 
    def clear(self) -> None:
        """
        Remove the current dataset and overwrite the systems collected data
        """
        self._check_writable()
        for path in self.json_files():
            path.unlink()
        if self.is_built():
            self.graph_file.unlink()
            
            
    def save_file(self, filename: str, content: bytes) -> Path:
        """
        Attempt to save files 
        """
        self._check_writable()
        safe = Path(filename).name                    
        if not safe.endswith(".json"):
            raise ValueError("Only .json files can be added to a dataset")
        self.create()
        path = self.data_dir / safe
        path.write_bytes(content)
        return path

    # ======================
    # This can be used to explore available datasets in the system
    # This means we can swap from testing to development or other sets etc.
    # For simpplicity you will just pass in "raw" as a string to work from
    # The provided dataset. 
    
    @classmethod
    def all(cls) -> list[Dataset]:
        if not config.DATASETS_DIR.is_dir():
            return []
        return [cls(p.name) for p in sorted(config.DATASETS_DIR.iterdir())
                if p.is_dir() and VALID_NAME.match(p.name)]

    def __repr__(self):
        return f"Dataset({self.name!r})"


# =======================
# Schemas can be accessed seperately and we dont really care if a schema comes solow

def schema_path(schema_name: str = config.DEFAULT_SCHEMA) -> Path:
    """Path of a schema .owl by name, e.g. schema_path("university")."""
    if not VALID_NAME.match(schema_name):
        raise ValueError(f"Invalid schema name: {schema_name!r}")
    return config.SCHEMAS_DIR / f"{schema_name}.owl"

def save_schema(schema_name: str, content: bytes) -> Path:
    if schema_name in config.PROTECTED_SCHEMAS:
        raise ProtectedNameError(f"'{schema_name}' is a default schema and can't be changed")
    path = schema_path(schema_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path