"""


"""

from collections import Counter
import json

from utility import config
import rdflib


class Cache:
    """
    this was just annoying me not being able to run the server and test
    so this ATTEMPTs to create a cache using nt such that the graph can load
    quickly and you're not waiting 30 mins or giving large memory to 
    the reasoner
    """
    def __init__(self, dataset):
        self.dataset = dataset
        self.asserted_file = config.GRAPHS_DIR / f"{dataset.name}_asserted.nt"
        self.reasoned_file = config.GRAPHS_DIR / f"{dataset.name}_reasoned.nt"
        self.errors_file = config.GRAPHS_DIR / f"{dataset.name}_errors.json"
        self.errors_before_file = config.GRAPHS_DIR / f"{dataset.name}_errors_before.json"
        self.files = [self.asserted_file, self.reasoned_file, self.errors_file, self.errors_before_file]


    def is_fresh(self):
        for f in self.files:
            if not f.exists():
                return False
        built = self.dataset.graph_file.stat().st_mtime
        for f in self.files:
            if f.stat().st_mtime <= built:
                return False
        return True

    def save(self, asserted, reasoned, errors, errors_before):
        asserted.serialize(destination=str(self.asserted_file), format="nt")
        reasoned.serialize(destination=str(self.reasoned_file), format="nt")
        self.errors_file.write_text(json.dumps(dict(errors)))
        self.errors_before_file.write_text(json.dumps(dict(errors_before)))

    def read(self):
        asserted = rdflib.Graph().parse(str(self.asserted_file), format="nt")
        reasoned = rdflib.Graph().parse(str(self.reasoned_file), format="nt")
        errors = Counter(json.loads(self.errors_file.read_text()))
        errors_before = Counter(json.loads(self.errors_before_file.read_text()))
        return asserted, reasoned, errors, errors_before