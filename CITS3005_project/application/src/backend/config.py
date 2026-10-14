"""
Config just holds basic set objects.

################
LEAVE THIS FILE AS IS
################
"""

from pathlib import Path

# =========================
# NAMESPACES (IRIs)
# =========================
BASE_IRI = "http://uwa/uni.ot#"         # classes, properties, rules
SCHEMA_IRI = BASE_IRI 
TEST_IRI = "http://uwa/test.ot#"        # IRI for tesing purposes
DATA_IRI_BASE = "http://uwa/uni.data/"  # each dataset gets <base><name>#
# =========================
# PATHS
# Note these will have to be constructed dependant on datasets 
# and can be named after the dataset we are working with.
# =========================
BASE_DIR = Path(__file__).resolve().parent # Create base data link 
DATA_DIR = BASE_DIR / "data"
DATASETS_DIR = DATA_DIR / "datasets"
SCHEMAS_DIR = DATA_DIR / "schemas"
GRAPHS_DIR = DATA_DIR / "graphs"

# Defaults when not input -> Will always load ATLEAST this
DEFAULT_DATASET = "raw"
DEFAULT_SCHEMA = "university"

# There are some datasets we dont want overwritten.
# This is essentially the supplied dataset from project 
# and the schema we are finalising before sending.
PROTECTED_DATASETS = {DEFAULT_DATASET}
PROTECTED_SCHEMAS = {DEFAULT_SCHEMA}

REASONER = "pellet"        # "hermit" (default) or "pellet"
INFER_PROPERTY_VALUES = True
INFER_DATA_PROPERTY_VALUES= True

# Both reasoners need Java. Leave as None if `java` is on the system PATH;
# otherwise set the full path to the java executable.
JAVA_EXE = None            # e.g. r"C:\Program Files\Java\jdk-21\bin\java.exe"

if JAVA_EXE:
    import owlready2
    owlready2.JAVA_EXE = JAVA_EXE
    
  