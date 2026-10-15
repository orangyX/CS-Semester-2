"""
This runs the full pipeline in parsing and 
creating the graph
"""

from utility import utils
from ontology.rules import Rules
from utility import config
from utility.parser import ParseDataSet
from ontology.base import OntologyBase
from builder.build import GraphBuilder
from utility.datasets import Dataset
from shapes import shapes

SCHEMA_NAME = "base"
RULES_NAME = "rules"
DATASET_NAME = "raw"


def main():
    
    
    schema_path = OntologyBase(config.SCHEMA_IRI).save(SCHEMA_NAME)
    print(f"Schema saved to {schema_path}")

    rules_path = Rules(config.RULES_IRI, SCHEMA_NAME, include_outcomes=False).save(RULES_NAME)
    print(f"Rules saved to {rules_path}")
    
    clean = ParseDataSet(DATASET_NAME).parse()
    print(f"Parsed: { {k: len(v) for k, v in clean.items()} }")

    builder = GraphBuilder(SCHEMA_NAME, DATASET_NAME, clean)
    builder.build()
    print(f"Graph saved to {builder.save()}")
    
    world, schemas, graph = utils.load_everything(Dataset(DATASET_NAME), [SCHEMA_NAME, RULES_NAME])
    utils.run_reasoner(world)
    conforms, summary, report = shapes.check(world)
    print("SHACL: all checks pass" if conforms else "SHACL problems:")
    for message, count in summary.items():
        print(f"  {count:4}  {message}")
   
def build():
    main()
         
if __name__ == "__main__":
    main()