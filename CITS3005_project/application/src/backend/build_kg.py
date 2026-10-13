from owlready2 import * 
from university_ot import OntologySchema # The schema load
import json
from config import DEGREES_JSON, BASE_IRI, MAJORS_JSON, SCHEMA_FILE, INFER_PROPERTY_VALUES, REASONER, INFER_DATA_PROPERTY_VALUES, UNITS_JSON

def build_graph():
    world = World()
    onto = world.get_ontology(BASE_IRI)
    ontology = OntologySchema(world, onto,"university.owl", "rdfxml")

    load_data(world, onto)
        
    onto.save(file="university_ot.owl", format="rdfxml")
    run_reasoner(world)

def load_data(world: World, onto: Ontology) -> None:
    degrees = json.loads(DEGREES_JSON.read_text(encoding="utf-8"))
    majors = json.loads(MAJORS_JSON.read_text(encoding="utf-8"))
    units = json.loads(UNITS_JSON.read_text(encoding="utf-8"))

    # THIS WILL CERTAINLY BE CLEANED, THIS IS JUST TO GET IT ROLLING

    with onto:
        # Load degree data
        for deg_code, data in degrees.items():
            # Classes we must instantiate prior
            school = onto.School(data.get("school"))
            location = onto.Location(data.get("location"))
            study_type = onto.StudyType(data.get("study_type"))
            avail_majors = data.get("majors")
            none_major = onto.Major("None")

            degree = onto.Degree(deg_code) # A degree object, identified by its code
            degree.degreeCode = deg_code
            degree.degreeTitle = data.get("title")
            degree.degreeSchool.append(school) # Non-functional, so append to a list
            degree.degreeCreditsToComplete = int(data.get("total_points"))
            degree.degreeFullTimeDuration = int(data.get("standard_full_time_completion")[0]) # Is a list of a single element
            degree.degreeLocation.append(location)
            degree.degreeStudyType = study_type

            if avail_majors:
                for m in avail_majors:
                    major = onto.Major(m) # Convert each to a Major object, then append
                    degree.degreeHasMajor.append(major)
            else:
                degree.degreeHasMajor = [none_major] # Some degrees are part of no majors

        for major_code, data in majors.items():
            # Attached to IRI, so if they already exist, it fetches the iri "http://uwa/uni.ot#/Field"
            school = onto.School(data.get("school"))
            bridging_units = data.get("bridging")

            major = onto.Major(major_code)
            major.majorCode = major_code
            major.majorTitle = data.get("title")
            major.majorSchool.append(school)
            major.majorDescription.append(data.get("description"))

            for o in data.get("outcomes"):
                major.majorOutcomes.append(o)

            for u in bridging_units:
                unit = onto.Unit(u)

                major.majorBridgingUnits.append(unit)

        for unit_code, data in units.items():
            print(unit_code, data)

            unit_school = onto.School(data.get("school"))
            unit_semesters = data.get("semester")
            unit_locations = onto.Location(data.get("locations"))
            unit_modes = data.get("modes")
            unit_outcomes = data.get("outcomes")
            assessments = data.get("assessment")
            unit_majors = onto.Major(data.get("majors"))
            preq_unit = data.get("prerequisite_units")
            contact_types = data.get("contact") # Another dictionary, which needs processing

            unit = onto.Unit(unit_code)
            unit.unitCode = unit_code
            unit.unitTitle = data.get("title")
            unit.unitSchool.append(unit_school)
            unit.unitLevel = int(data.get("level"))
            unit.unitDescription.append(data.get("description"))
            unit.unitAwardsCredits = int(data.get("credit"))
            unit.unitOfferedAtLocation.append(unit_locations)


            # MANY BUGS HERE THAT NEED FIXING (LATER); ALSO, CAN BE DONE IN ONE LOOP VIA ZIP
            # if unit_semesters:
            #     for s in unit_semesters:
            #         unit.unitSemesterAvailability.append(s)
            # else:
            #     unit.unitSemesterAvailability.append(0)

            # for m in unit_modes:
            #     unit.unitModes.append(m)

            # for o in unit_outcomes:
            #     unit.unitOutcomes.append(o)

            # for a in assessments:
            #     unit.unitAssessmentTypes.append(a)

            # for m in major:
            #     major = onto.Major(m)
            #     unit.unitPartOfMajor.append(major)

            



def run_reasoner(world):
    if REASONER == "pellet":
        sync_reasoner_pellet(world,
                             infer_property_values=INFER_PROPERTY_VALUES,
                             infer_data_property_values=INFER_DATA_PROPERTY_VALUES)
    elif REASONER == "hermit":
        sync_reasoner_hermit(world, infer_property_values=INFER_PROPERTY_VALUES)

build_graph()