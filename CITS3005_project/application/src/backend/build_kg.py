from owlready2 import * 
from university_ot import OntologySchema # The schema load
import json
from config import DEGREES_JSON, BASE_IRI, MAJORS_JSON, SCHEMA_FILE, INFER_PROPERTY_VALUES, REASONER, INFER_DATA_PROPERTY_VALUES, UNITS_JSON

def build_graph():
    world = World()
    onto = world.get_ontology(BASE_IRI)
    ontology = OntologySchema(world, onto,"university.owl", "rdfxml")

    degrees = json.loads(DEGREES_JSON.read_text(encoding="utf-8"))
    majors = json.loads(MAJORS_JSON.read_text(encoding="utf-8"))
    units = json.loads(UNITS_JSON.read_text(encoding="utf-8"))

    load_degrees(degrees, onto)
    load_majors(majors, onto)
    load_units(units, majors, onto)
        
    onto.save(file="university_ot.owl", format="rdfxml")
    run_reasoner(world)

def load_degrees(degrees: dict, onto: Ontology) -> None:
    """
        Reads from degrees.json, parses according to ontology structure
    """
    for deg_code, data in degrees.items():
        # Classes we must instantiate prior
        school = onto.School(clean(data.get("school")))
        location = onto.Location(clean(data.get("locations")))
        study_type = onto.StudyType(clean(data.get("study_type")))

        # A list of majors, which are to be iterated through
        avail_majors = data.get("majors")

        degree = onto.Degree(deg_code) # A degree object, identified by its code
        degree.degreeCode = deg_code
        degree.degreeTitle = data.get("title")
        degree.degreeSchool.append(school) # Non-functional, so append to a list
        degree.degreeCreditsToComplete = data.get("total_points")
        degree.degreeFullTimeDuration = int(data.get("standard_full_time_completion")[0]) if data.get("standard_full_time_completion") else None # Is a list of a single element
        degree.degreeLocation.append(location)
        degree.degreeStudyType = study_type

        if avail_majors: 
            for m in avail_majors:
                major = onto.Major(clean(m)) # Convert each to a Major object, then append
                degree.degreeHasMajor.append(major)

        # Every degree has at least one major; adding a degree that does not have any degrees will result in a violation

def load_majors(majors: dict, onto: Ontology) -> None:
    """
        Reads from majors.json, parses according to ontology structure
    """
    for major_code, data in majors.items():
        # Attached to IRI, so if they already exist, it fetches the iri "http://uwa/uni.ot#/Field"
        school = onto.School(clean(data.get("school")))

        # The list of majors which act as bridging units for a particular unit
        outcomes = data.get("outcomes")
        bridging_units = data.get("bridging")

        major = onto.Major(major_code)
        major.majorCode = major_code
        major.majorTitle = data.get("title")
        major.majorSchool.append(school)
        major.majorDescription.append(data.get("description"))

        if outcomes:
            major.majorOutcomes = [o for o in outcomes]

        if bridging_units:
            for u in bridging_units:
                bridging_unit = onto.Unit(u)

                major.majorBridgingUnits.append(bridging_unit)

def load_units(units: dict, majors: dict, onto: Ontology) -> None:
    """
        Reads from units.json, parses according to ontology structure
    """
    for unit_code, data in units.items():
        unit = onto.Unit(unit_code)

        school = onto.School(clean(data.get("school")))

        locations = data.get("locations")
        contact_modes = data.get("contact")
        semesters = data.get("semesters")
        assessment_types = data.get("assessment")
        outcomes = data.get("outcomes")

        if semesters:
            unit.unitSemesterAvailability = [s for s in semesters]

        if locations:
            for l in locations:
                location = onto.Location(clean(l))

                unit.unitLocation.append(location)

        # Process the contact mode, along with the hours per week
        if contact_modes:
            for c_type, hour in contact_modes.items():
                contact_mode = onto.ContactMode(unit_code + clean(c_type)) # This unit owns this contact mode
                contact_mode.contactModeHours = hour
                contact_mode.contactModeType = c_type

                unit.unitContactTypes.append(contact_mode)

        if assessment_types:
            unit.unitAssessmentTypes = [a for a in assessment_types]

        if outcomes:
            unit.unitOutcomes = [o for o in outcomes]

        unit.unitCode = unit_code
        unit.unitTitle = data.get("title")
        unit.unitSchool.append(school)
        unit.unitLevel = int(data.get("level")) if data.get("level") else None
        unit.unitDescription = data.get("description")
        unit.unitAwardsCredits = int(data.get("credit")) if data.get("credit") else None

def clean(string: str) -> str:
    """
        Converts a string to an IRI-friendly format (no space, brackets)
    """
    return string.replace("(", "").replace(")", "").replace(" ", "").replace("'", "").replace(",", "")

def run_reasoner(world):
    if REASONER == "pellet":
        sync_reasoner_pellet(world,
                             infer_property_values=INFER_PROPERTY_VALUES,
                             infer_data_property_values=INFER_DATA_PROPERTY_VALUES)
    elif REASONER == "hermit":
        sync_reasoner_hermit(world, infer_property_values=INFER_PROPERTY_VALUES)

build_graph()