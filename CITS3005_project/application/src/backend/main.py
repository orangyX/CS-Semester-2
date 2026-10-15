"""
This runs the full pipeline in parsing and 
creating the graph
"""

import queries
from utility.caching import Cache
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


def build():
    
    
    schema_path = OntologyBase(config.SCHEMA_IRI).save(SCHEMA_NAME)
    print(f"Schema saved to {schema_path}")

    rules_path = Rules(config.RULES_IRI, SCHEMA_NAME, include_outcomes=False).save(RULES_NAME)
    print(f"Rules saved to {rules_path}")
    
    clean = ParseDataSet(DATASET_NAME).parse()
    print(f"Parsed: { {k: len(v) for k, v in clean.items()} }")

    builder = GraphBuilder(SCHEMA_NAME, DATASET_NAME, clean)
    builder.build()
    print(f"Graph saved to {builder.save()}")
    

def reason(dataset, schemas):
    cache = Cache(dataset)
    if cache.is_fresh():
        print("Using cached reasoning results")
        return cache.read()

    world, _, _ = utils.load_everything(dataset, schemas)
    asserted = queries.to_graph(world)          # before reasoning
    utils.run_reasoner(world)
    reasoned = queries.to_graph(world)          # after reasoning
    conforms, errors, report = shapes.check(world)

    print("SHACL: all checks pass" if conforms else "SHACL problems:")
    for message, count in errors.items():
        print(f"  {count:4}  {message}")

    cache.save(asserted, reasoned, errors)      # after the loop, not inside it
    return asserted, reasoned, errors

def main():
    build()
    reason(Dataset(DATASET_NAME), [SCHEMA_NAME, RULES_NAME])
         
if __name__ == "__main__":
    main()