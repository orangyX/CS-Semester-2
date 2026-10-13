"""
config.py - shared settings for every script in the project.

There are IRI, datasets, pathing and objects that will exist outside
the application that we can use to experiment with, you can 
import as:
    import config
"""

from pathlib import Path

# This is a file name for data that can be changed. 
DATASET = "raw"            


# =========================
# NAMESPACES (IRIs)
# =========================
BASE_IRI   = "http://uwa/uni.ot#"                  # classes, properties, rules

# =========================
# PATHS
# =========================
BASE_DIR   = Path(__file__).resolve().parent
DATA_DIR   = BASE_DIR / "data" / DATASET     
OUTPUT_DIR = BASE_DIR / "output"             # generated .owl files

# Input JSON  (OPEN: confirm file names match the handbook.zip files)
DEGREES_JSON = DATA_DIR / "degrees.json"
MAJORS_JSON  = DATA_DIR / "majors.json"
UNITS_JSON   = DATA_DIR / "units.json"

# Output OWL
SCHEMA_FILE = OUTPUT_DIR / "university_ot.owl"         
DATA_FILE   = OUTPUT_DIR / f"university_kg_{DATASET}.owl"


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