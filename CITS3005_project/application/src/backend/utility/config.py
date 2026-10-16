"""
Config just holds basic set objects.

"""

from pathlib import Path

# Which dataset and schemas the pipeline and app use.
# Change these to run on a different dataset (data/datasets/<DATASET_NAME>/).
DATASET_NAME = "raw"
SCHEMA_NAME = "base"
RULES_NAME = "rules"

# =========================
# NAMESPACES (IRIs)
# =========================
BASE_IRI = "http://uwa/uni.ot#"         # classes, properties, rules
SCHEMA_IRI = BASE_IRI 
RULES_IRI = "http://uwa/uni.rules#"
TEST_IRI = "http://uwa/test.ot#"        # IRI for tesing purposes
DATA_IRI_BASE = "http://uwa/uni.data/"  # each dataset gets <base><name>#

# =========================
# PATHS
# Note these will have to be constructed dependant on datasets 
# and can be named after the dataset we are working with.
# Assume runningin from application
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent # Create base data link 
DATA_DIR = BASE_DIR / "data"
DATASETS_DIR = DATA_DIR / "datasets"
SCHEMAS_DIR = DATA_DIR / "schemas"
GRAPHS_DIR = DATA_DIR / "graphs"

REASONER = "hermit"        # "hermit" (default) or "pellet"
INFER_PROPERTY_VALUES = True
INFER_DATA_PROPERTY_VALUES= True

JAVA_EXE = None          

if JAVA_EXE:
    import owlready2
    owlready2.JAVA_EXE = JAVA_EXE