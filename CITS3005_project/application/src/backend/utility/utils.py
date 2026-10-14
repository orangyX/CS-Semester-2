"""
File should be a class called Utility

Shouldn't hold and data but just functions that are used 
repeatedly so that we can just call the function instead
of writing heaps of the same code.
"""

from owlready2 import World, sync_reasoner_hermit, sync_reasoner_pellet
 
import config
from datasets import Dataset, schema_path
 
 
# =========================
# SAVING
# =========================
def save_schema_onto(onto, name: str):
    """
    Save a schema in data/schemas/<name>.owl.
    Requires a name
    """
    path = schema_path(name)
    path.parent.mkdir(parents=True, exist_ok=True)
    onto.save(file=str(path), format="rdfxml")
    return path
 
 
def save_graph_onto(onto, dataset: Dataset):
    """
    Save a graph in data/graphs/<dataset>.owl.
    Requires the ontology schema and the dataset thats being worked on
    """
    path = dataset.graph_file
    path.parent.mkdir(parents=True, exist_ok=True)
    onto.save(file=str(path), format="rdfxml")
    return path
 
 
# =========================
# LOADING
# =========================
def load_schema(world: World, name: str):
    """
    Load from data/schemas/<name>.owl 
    Loads the schema onto the world you're creating
    Requires a name to find the file.
    """
    path = schema_path(name)
    if not path.is_file():
        raise FileNotFoundError(f"No schema named {name!r} at {path}")
    return world.get_ontology(path.as_uri()).load()
 
 
def load_schemas(world: World, names: list[str]) -> list:
    """
    This is just for if we want to split the ontology into more
    managable objects, we can load all and then push onto the world
    """
    return [load_schema(world, name) for name in names]
 
 
def load_graph(world: World, dataset: Dataset):
    """
    This loads a graph onto a world using a specific dataset.
    """
    if not dataset.is_built():
        raise FileNotFoundError(f"Dataset {dataset.name!r} has no built graph at {dataset.graph_file}")
    return world.get_ontology(dataset.graph_file.as_uri()).load()
 
 
def load_everything(dataset: Dataset, schema_names: list[str]) -> tuple:
    """
    Creates a fresh world
    Loads the schemas you're using and pushes them onto a graph 
    Uses base first then extensions 
    using the schemas.
    Returns (world, schema ontologies, graph ontology).
    """
    world = World()
    schemas = load_schemas(world, schema_names)
    graph = load_graph(world, dataset)
    return world, schemas, graph
 
 
# =========================
# CHECKS
# =========================
def missing_vocabulary(onto, names: list[str]) -> list[str]:
    """
    Names (classes, properties, individuals) the ontology doesn't define.
    Use before parsing to check a schema has everything the parser needs.
    """
    return [name for name in names if onto[name] is None]
 
 
# =========================
# REASONING
# =========================
def run_reasoner(world: World, store_in=None):
    """Run the configured reasoner over the whole world.
 
    store_in: an ontology to hold the inferred facts. Pass a separate one
    (e.g. world.get_ontology("http://uwa/uni.inferred#")) so inferences never
    end up inside a schema or graph you later save.
    """
    def _reason():
        if config.REASONER == "pellet":
            sync_reasoner_pellet(world,
                                 infer_property_values=config.INFER_PROPERTY_VALUES,
                                 infer_data_property_values=config.INFER_DATA_PROPERTY_VALUES)
        elif config.REASONER == "hermit":
            sync_reasoner_hermit(world, infer_property_values=config.INFER_PROPERTY_VALUES)
        else:
            raise ValueError(f"Unknown reasoner: {config.REASONER!r}")
 
    if store_in is None:
        _reason()
    else:
        with store_in:
            _reason()