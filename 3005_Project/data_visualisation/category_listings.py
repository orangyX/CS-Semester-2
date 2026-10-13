import json
from pathlib import Path
from typing import List

IN_DEGREES_DIR = Path("handbook/degrees.json")
IN_MAJORS_DIR = Path("handbook/majors.json")
IN_UNITS_DIR = Path("handbook/units.json")

OUTPATH_DIR = Path("data_visualisation/data/properties/")

DEGREES = Path("Degrees")
MAJORS = Path("Majors")
UNITS = Path("Units")

property_types = [
    "code",
    "title",
    "school",
    "study_type",
    "total_points",
    "standard_full_time_completion",
    "locations",
    "majors",
    "description",
    "outcomes",
    "courses",
    "bridging",
    "units",
    "level",
    "credit",
    "semesters",
    "locations",
    "modes",
    "assessment",
    "contact",
    "prerequisites_text",
    "prerequisite_courses",
    "prerequisite_units",
    "advisable_prior_study",
    "note"
]

def main(in_path: Path, out_path: Path, cat: int) -> None:
    
    object_count = 0
    properties = []

    data = json.loads(in_path.read_text(encoding="utf-8"))

    print(data)
    for items in data:
        object_count += 1





     
    print(properties)

    report = {
        "Object Count": object_count,
        "Properties Count": len(properties),
        "Properties": properties,
    }
    
    out_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding="utf-8")

    print(f"\nSaved report to {out_path}")


# Process each handbook json file. 
main(IN_DEGREES_DIR, OUTPATH_DIR, DEGREES)
main(IN_MAJORS_DIR, OUTPATH_DIR, MAJORS)
main(IN_UNITS_DIR, OUTPATH_DIR, UNITS)
