from owlready2 import * 
from university_ot import OntologySchema # The schema load
import json
from backend.utility.config import DEGREES_JSON, BASE_IRI, MAJORS_JSON, SCHEMA_FILE, INFER_PROPERTY_VALUES, REASONER, INFER_DATA_PROPERTY_VALUES, UNITS_JSON
import itertools

def build_graph() -> None:
    world = World()
    onto = world.get_ontology(BASE_IRI)
    ontology = OntologySchema(world, onto,"university.owl", "rdfxml")

    degrees = json.loads(DEGREES_JSON.read_text(encoding="utf-8"))
    majors = json.loads(MAJORS_JSON.read_text(encoding="utf-8"))
    units = json.loads(UNITS_JSON.read_text(encoding="utf-8"))

    load_degrees(degrees, onto)
    load_majors(majors, onto)
    load_units(units, majors, onto)
    fill_combined_bachelors(degrees, onto)
        
    onto.save(file="university_ot.owl", format="rdfxml")
    run_reasoner(world)

    # TESTING ---------------------------------------------------------------------------
    combined = [d for d in onto.Degree.instances() if isinstance(d.degreeStudyType, onto.CombinedBachelor)]

    for cb in combined:
        degs = [d for d in cb.combinedBachelorIncludes]

        for d in degs:
            print(f"{cb} includes {d.degreeTitle}, total_points = {cb.degreeCreditsToComplete} over {cb.degreeFullTimeDuration} years")

def load_degrees(degrees: dict, onto: Ontology) -> None:
    """
        Reads from degrees.json, parses according to ontology structure
    """
    for deg_code, data in degrees.items():  
        degree = onto.Degree(deg_code) # A degree object, identified by its code

        # Classes we must instantiate prior
        school = onto.School(name_cleaner(data.get("school")))
        study_type = onto.StudyType(name_cleaner(data.get("study_type")))

        # A list of majors, which are to be iterated through
        avail_majors = data.get("majors") if data.get("majors") else None
        locations = string_cleaner(data.get("locations")).split(",") if data.get("locations") else None

        if locations:
            for l in locations:
                location = onto.Location(name_cleaner(l))

                degree.degreeLocation.append(location)

        if avail_majors: 
            for m in avail_majors:
                major = onto.Major(name_cleaner(m)) # Convert each to a Major object, then append

                degree.degreeHasMajor.append(major) # And owlready2 can infer data for the inverse relation

        degree.degreeCode = deg_code
        degree.degreeTitle = string_cleaner(data.get("title"))
        degree.degreeSchool.append(school) # Non-functional, so append to a list
        degree.degreeCreditsToComplete = data.get("total_points")
        degree.degreeFullTimeDuration = int(data.get("standard_full_time_completion")[0]) if data.get("standard_full_time_completion") else None # Is a list of a single element
        degree.degreeStudyType = study_type

        # Every degree has at least one major; adding a degree that does not have any degrees will result in a violation

def load_majors(majors: dict, onto: Ontology) -> None:
    """
        Reads from majors.json, parses according to ontology structure
    """
    for major_code, data in majors.items():
        # Attached to IRI, so if they already exist, it fetches the iri "http://uwa/uni.ot#/Field"
        school = onto.School(name_cleaner(data.get("school")))

        # The list of majors which act as bridging units for a particular unit
        outcomes = data.get("outcomes")
        bridging_units = data.get("bridging")
        units = data.get("units")

        major = onto.Major(major_code)
        major.majorCode = major_code
        major.majorTitle = string_cleaner(data.get("title"))
        major.majorSchool.append(school)
        major.majorDescription.append(string_cleaner(data.get("description")))

        if outcomes:
            major.majorOutcomes = [o for o in outcomes]

        if bridging_units:
            for u in bridging_units:
                bridging_unit = onto.Unit(u)

                major.majorBridgingUnits.append(bridging_unit)

        if units:
            for u in units:
                unit = onto.Unit(name_cleaner(u))

                major.majorHasCoreUnit.append(unit) # owlready2 will populate the inverse relation, too
        
        # Missing: majorProgression, majorCreditsAtLevel

def load_units(units: dict, majors: dict, onto: Ontology) -> None:
    """
        Reads from units.json, parses according to ontology structure
    """
    
    for unit_code, data in units.items():
        unit = onto.Unit(unit_code)

        school = onto.School(name_cleaner(data.get("school")))

        locations = data.get("locations")
        contact_modes = data.get("contact")
        semesters = data.get("semesters")
        assessment_types = data.get("assessment")
        outcomes = data.get("outcomes")
        preq_units = list(itertools.chain.from_iterable(data.get("prerequisite_units"))) if data.get("prerequisite_units") else None

        if semesters:
            unit.unitSemesterAvailability = [s for s in semesters]

        if locations:
            for l in locations:
                location = onto.Location(name_cleaner(l))

                unit.unitLocation.append(location)

        # Process the contact mode, along with the hours per week
        if contact_modes:
            for c_type, hour in contact_modes.items():
                contact_mode = onto.ContactMode(unit_code + name_cleaner(c_type)) # This unit owns this contact mode
                contact_mode.contactModeHours = hour
                contact_mode.contactModeType = c_type

                unit.unitContactTypes.append(contact_mode)

        if assessment_types:
            unit.unitAssessmentTypes = [a for a in assessment_types]

        if outcomes:
            unit.unitOutcomes = [o for o in outcomes]

        if preq_units: # Some of these units are not in units.json?
            for u in preq_units:
                if u in units:
                    preq_unit = onto.Unit(u)

                    unit.unitHasPrerequisite.append(preq_unit)
                else:
                    # If a unit is a 'floating unit', it is still a prerequisite to the specified unit, so we shall include it to more accurately model information
                    floating_unit = onto.FloatingUnit(u)
                    floating_unit.unitCode = u

                    unit.unitHasPrerequisite.append(floating_unit)

        unit.unitCode = unit_code
        unit.unitTitle = string_cleaner(data.get("title"))
        unit.unitSchool.append(school)
        unit.unitLevel = int(data.get("level")) if data.get("level") else None
        unit.unitDescription = string_cleaner(data.get("description"))
        unit.unitAwardsCredits = int(data.get("credit")) if data.get("credit") else None

def fill_combined_bachelors(degrees: dict, onto: Ontology) -> None:
    """
        Establishes a link between a combined degree and its degrees (already within owl, so fetch the object itself)
    """
    combined_bachelors = [d for d in onto.Degree.instances() if isinstance(d.degreeStudyType, onto.CombinedBachelor)]
    title_degree_mapping = {data["title"]: code for code, data in degrees.items()}

    for cb in combined_bachelors:
        titles = cb.degreeTitle.split("/ ") if "/" in cb.degreeTitle else cb.degreeTitle.split(" and ")

        for t in titles:
            code = title_degree_mapping.get(t.strip())
            degree_constituent = onto[code] if code else None

            if degree_constituent:
                cb.combinedBachelorIncludes.append(degree_constituent)            

def name_cleaner(string: str) -> str:
    """
        Converts a string to an IRI-friendly format (no space, brackets)
    """
    return string.replace("(", "").replace(")", "").replace(" ", "").replace("'", "").replace(",", "")

def string_cleaner(string: str) -> str:
    """
        Removes invisible characters which will cause MalformedLiteralException
    """

    return string.replace("\x0b", " ")

def run_reasoner(world):
    if REASONER == "pellet":
        sync_reasoner_pellet(world,
                             infer_property_values=INFER_PROPERTY_VALUES,
                             infer_data_property_values=INFER_DATA_PROPERTY_VALUES)
    elif REASONER == "hermit":
        sync_reasoner_hermit(world, infer_property_values=INFER_PROPERTY_VALUES)

build_graph()