from owlready2 import World
from pathlib import Path

KG_PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "graphs" / "raw.owl"
SCH_PATH = Path(__file__).resolve().parent.parent / "backend" / "data" / "schemas" / "base2.owl"

world = World()
schema = world.get_ontology("http://uwa/uni.ot#").load(fileobj=open(SCH_PATH, "rb"))
data = world.get_ontology("http://uwa/uni.data/raw#").load(fileobj=open(KG_PATH, "rb"))

