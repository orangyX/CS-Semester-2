"""
config.py - shared settings for every script in the project.

There are IRI, datasets, pathing and objects that will exist outside
the application that we can use to experiment with, you can 
import as:
    import config
"""

# =========================
# IMPORTS
# =========================
from pathlib import Path


# =========================
# DATASET
# =========================
# DECISION: swappable datasets. Each dataset gets its own folder under data/
# and its own data namespace, all sharing the same schema.
DATASET = "raw"            # e.g. "raw" (provided JSON) or "clean" (our processed version)


# =========================
# NAMESPACES (IRIs)
# =========================
SCHEMA_IRI   = "http://uwa/uni.ot#"                  # classes, properties, rules
DATA_IRI     = f"http://uwa/uni.data/{DATASET}#"      # individuals from the chosen dataset
INFERRED_IRI = f"http://uwa/uni.inferred/{DATASET}#"  # where the reasoner's conclusions go

# OPEN: if we split data into modules (locations, units, majors, degrees),
# give each its own IRI here and register them as SPARQL prefixes, e.g.
# UNITS_IRI = f"http://uwa/uni.data/{DATASET}/units#"
# EXTRA_PREFIXES = {"units": UNITS_IRI}


# =========================
# PATHS
# =========================
# All paths are relative to this file, so scripts work from any working directory.
BASE_DIR   = Path(__file__).resolve().parent
DATA_DIR   = BASE_DIR / "data" / DATASET     # the chosen dataset's JSON files
OUTPUT_DIR = BASE_DIR / "output"             # generated .owl files

# Input JSON  (OPEN: confirm file names match the handbook.zip files)
DEGREES_JSON = DATA_DIR / "degrees.json"
MAJORS_JSON  = DATA_DIR / "majors.json"
UNITS_JSON   = DATA_DIR / "units.json"

# Output OWL
SCHEMA_FILE = OUTPUT_DIR / "university_ot.owl"            # ontology deliverable
DATA_FILE   = OUTPUT_DIR / f"university_kg_{DATASET}.owl"  # written by build_kg.py

# OPEN: if we use data modules, list every data file instead (app.py checks for this):
# DATA_FILES = [OUTPUT_DIR / f"{DATASET}_units.owl", ...]


# =========================
# REASONER
# =========================
REASONER = "hermit"        # "hermit" (default) or "pellet"

# Both reasoners need Java. Leave as None if `java` is on the system PATH;
# otherwise set the full path to the java executable.
JAVA_EXE = None            # e.g. r"C:\Program Files\Java\jdk-21\bin\java.exe"

if JAVA_EXE:
    import owlready2
    owlready2.JAVA_EXE = JAVA_EXE