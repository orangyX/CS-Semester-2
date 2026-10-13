
import json
from pathlib import Path
from typing import List

IN_DEGREES_DIR = Path("handbook/degrees.json")
IN_MAJORS_DIR = Path("handbook/majors.json")
IN_UNITS_DIR = Path("handbook/units.json")

OUT_DEGREES_DIR = Path("data_visualisation/data/degrees.json")
OUT_MAJORS_DIR = Path("data_visualisation/data/majors.json")
OUT_UNITS_DIR = Path("data_visualisation/data/units.json")


def main(in_path: Path, out_path: Path) -> None:
    
    object_count = 0
    properties = []

    data = json.loads(in_path.read_text(encoding="utf-8"))

    for items in data:
        object_count += 1
        
        for key in data[items].keys():
            if key not in properties:
                properties.append(key)


     
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
main(IN_DEGREES_DIR, OUT_DEGREES_DIR)
main(IN_MAJORS_DIR, OUT_MAJORS_DIR)
main(IN_UNITS_DIR, OUT_UNITS_DIR)
