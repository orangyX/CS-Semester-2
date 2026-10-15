"""
This runs the full pipeline in parsing and 
creating the graph
"""

from utility import config
from utility.parser import ParseDataSet
from ontology.base2 import OntologyBase
from builder.build import GraphBuilder
from utility.datasets import Dataset

SCHEMA_NAME = "university_ot"
DATASET_NAME = "raw"


def main():
    
    schema_path = OntologyBase(config.SCHEMA_IRI).save(SCHEMA_NAME)
    print(f"Schema saved to {schema_path}")

    clean = ParseDataSet(DATASET_NAME).parse()
    print(f"Parsed: { {k: len(v) for k, v in clean.items()} }")

    builder = GraphBuilder(SCHEMA_NAME, DATASET_NAME, clean)
    builder.build()
    print(f"Graph saved to {builder.save()}")
    
if __name__ == "__main__":
    main()