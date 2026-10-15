"""
Use a schema and cleaned dataset to build the knowledge graph.

NOTE vocabulary defines exactly what it expects fromt he schema. 
New entites MUST be updated here if you make changes to your schema.

Currently i've just taken them from the base schema.

Theres some additional helpers here as the cleaning of data didnt justify or forsee
the issues at that time.
"""

from owlready2 import World

from utility import utils
from utility.datasets import Dataset

# Every class / property name the builder uses. A schema must define all of these.
VOCABULARY = [
    # classes
    "Degree", "Major", "Unit", "FloatingUnit", "School", "Location",
    "Bachelor", "Honours", "Combined",
    # shared
    "hasCode", "hasTitle", "belongsTo", "hasDescription", "hasOutcome", "locatedIn",
    # degree
    "hasStudyType", "hasTotalPoints", "hasDuration", "hasMajor", "includesDegree",
    # major
    "hasUnit", "requiresBridging",
    # unit
    "hasLevel", "hasCredit", "isAvailable", "hasPrerequisite",
    "offeredIn", "hasMode", "hasAssessment", "hasPrerequisiteText",
    # Updated vocabulary
    "ContactMode",
    "hasComponentTitle", "listedInDegree", "listedInMajor", "hasMajorTitle",
    "requiresDegree", "hasAdvisedUnit", "hasNote", "hasContact",
    "contactType", "contactHours",
]


class GraphBuilder:

    def __init__(self, schema_name: str, dataset_name: str, clean: dict):
        
        self.world = World()
        self.schema = utils.load_schema(self.world, schema_name)

        # Just log missing issues so that schemas can be built to specification.
        missing = [n for n in VOCABULARY if self.term(n) is None]
        if missing:
            raise ValueError(f"Schema {schema_name!r} is missing: {', '.join(missing)}")

        # Entities go in the dataset's own namespace, which imports the schema
        self.dataset = Dataset(dataset_name)
        self.onto = self.world.get_ontology(self.dataset.iri)
        self.onto.imported_ontologies.append(self.schema)

        self.clean = clean
        self.made = {}   

    # =========================
    # HELPERS
    # =========================
    def term(self, name):
        """
        A class or property from the schema
        """
        return self.world[self.schema.base_iri + name]

    def make(self, class_name: str, name: str):
        """
        Get an entity, creating it the first time it's asked for.
        """
        key = (class_name, name)
        if key not in self.made:
            self.made[key] = self.term(class_name)(name, namespace=self.onto)
        return self.made[key]

    def unit(self, code: str):
        """
        A unit by code. 
        Codes not in the dataset become FloatingUnits.
        """
        if code in self.clean["majors"] or code in self.clean["degrees"]:
            return None
        if code in self.clean["units"]:
            return self.make("Unit", code)
        floating = self.make("FloatingUnit", code)
        floating.hasCode = code
        return floating

    def units(self, codes) -> list:
        """
        Fix for units haveing multiple already existing units
        """
        result = []
        for code in codes:
            u = self.unit(code)
            if u is not None:
                result.append(u)
        return result
    def school(self, label):
        return self.make("School", "School_" + utils.slug(label)) if label else None

    def location(self, label):
        return self.make("Location", "Location_" + utils.slug(label))

    def contacts(self, unit_code: str, contact: dict) -> list:
        modes = []
        for i, (kind, hours) in enumerate(contact.items()):
            kind_id = utils.slug(kind) if kind else None
            c = self.make("ContactMode", f"{unit_code}_contact_{kind_id or i}")
            c.contactType = kind
            c.contactHours = hours
            modes.append(c)
        return modes
    # =========================
    # BUILD
    # =========================
    def build(self):
        self.study_types = {
            name: self.make(name, "StudyType_" + name)
            for name in ("Bachelor", "Honours", "Combined")
        }
        self.build_units()
        self.build_majors()
        self.build_degrees()

    def build_units(self):
        for code, r in self.clean["units"].items():
            u = self.make("Unit", code)
            u.hasCode = code
            u.hasTitle = r["title"]
            u.hasDescription = r["description"]
            u.hasLevel = r["level"]
            u.hasCredit = r["credit"]
            u.isAvailable = r["available"]
            u.hasPrerequisiteText = r["prerequisites_text"]
            u.belongsTo = self.school(r["school"])
            u.hasOutcome = r["outcomes"]
            u.offeredIn = r["semesters"]
            u.hasMode = r["modes"]
            u.hasAssessment = r["assessment"]
            u.locatedIn = [self.location(l) for l in r["locations"]]
            u.hasPrerequisite = self.units(r["prerequisites"])
            u.listedInMajor = [self.make("Major", c) for c in r["major_codes"]]
            u.hasMajorTitle = r["major_titles"]
            u.requiresDegree = [self.make("Degree", c) for c in r["prerequisite_degrees"]]
            u.hasAdvisedUnit = self.units(r["advisable_prior_study"])
            u.hasNote = r["note"]
            u.hasContact = self.contacts(code, r["contact"])

    def build_majors(self):
        for code, r in self.clean["majors"].items():
            m = self.make("Major", code)
            m.hasCode = code
            m.hasTitle = r["title"]
            m.hasDescription = r["description"]
            m.belongsTo = self.school(r["school"])
            m.hasOutcome = r["outcomes"]
            m.hasUnit = self.units(r["units"])
            m.requiresBridging = self.units(r["bridging"])
            m.listedInDegree = [self.make("Degree", c) for c in r["degrees"]]
            
    def build_degrees(self):
        for code, r in self.clean["degrees"].items():
            d = self.make("Degree", code)
            d.hasCode = code
            d.hasTitle = r["title"]
            d.hasTotalPoints = r["total_points"]
            d.hasDuration = r["duration_years"]
            d.belongsTo = self.school(r["school"])
            d.hasStudyType = self.study_types.get(r["study_type"])
            d.locatedIn = [self.location(l) for l in r["locations"]]
            d.hasMajor = [self.make("Major", m) for m in r["majors"]]
            d.includesDegree = [self.make("Degree", c) for c in r["components"]]
    # =========================
    # SAVE
    # =========================
    def save(self):
        return utils.save_graph_onto(self.onto, self.dataset)