"""
File to support the parsing of the data set and preparing it
for conversion to a graph using a selected schema.

Half of this code is modeled after my attempts to parse the made in abyss wiki
which i failed at. But this dataset is abit cleaner so i'm hoping for the best.
"""

# Regular expression is an import to do with strings and making regular expressions
# Will be used to reason and fix the broken data found 
import re               # NOTE THIS is something to connsider for report.
import json

from pathlib import Path

from utility import config, utils

# Make sure the name input is valid
# To be valid a name must consist of any vocabulary which holds
# the following single string types fo any length really.
# This is cool as you can't point to anything OUTSIDE the folder by accident.
VALID_NAME = re.compile(r"^[A-Za-z0-9_-]+$") 

############################################################
# Section here is used to give mappings and turn data into a nice format when things are unknown.
# Add any mapping of odd values to internal expected format.
# Be careful not to over do this -> can turn into fuzzy reasoning
# There will still be alot of lost data from poor data representation
# But we can take common oddities and represent them more cleanly

MAPPED_VALUES = {
}

# Map code types to study type
STUDY_TYPES = {
    "BP": "Bachelor",
    "BH": "Honours",
    "CB": "Combined",
}

# Holds unavailable info
UNAVAILABLE = {"Not available in 2026"}

# Find the first number in a string
# Note that it cuts decimals so ALL numbers must be rational
FIRST_NUMBER = re.compile(r"\d+")

# Find a string patter where its in the pattern of 
# " \ " OR " and " -> check for if next string object is "Bachelor"
# Use to safely split bachelors in a string when multiple are written.
COMBINED_SPLIT = re.compile(r"\s*/\s*|\s+and\s+(?=Bachelor)")

############################################################

# HELPERS
def text(value):
    """
    Tidy a single string
    """
    if value is None:
        return None
    value = " ".join(str(value).split())
    value = MAPPED_VALUES.get(value, value)
    return value or None


def number(value):
    """
    Find the first number and remove string additions
    "3 weeks" -> "3"
    """
    if isinstance(value, int):
        return value
    match = FIRST_NUMBER.search(str(value)) if value is not None else None
    return int(match.group()) if match else None


def text_list(values):
    """
    Clean a list of strings using text(value)
    """
    seen = []
    for v in values or []:
        v = text(v)
        if v and v not in seen:
            seen.append(v)
    return seen


def flatten(values):
    """
    Flatten list shapes 
    
    Note this has a caviate. The shape of prerequisites are in list shapes
    which would mean like [A], [B, C]. where A is a prerequisite and EITHER B OR C is one.
    Under the graph strucutre we kinda lose that meaning so this is a direct limitation.
    
    Set {A, B ,C} are ALL prerequisites. But prerequisite strucutre undefined.
    """
    flat = []
    for v in values or []:
        flat.extend(v if isinstance(v, list) else [v])
    return flat

# ==========================
# THE ACTUAL CLASS FINALLY LMAO
# ===========================

class ParseDataSet:
    """
    Class requires a directory name to function. This is a later worry.
    
    When called enter "raw" as a input.
    
    Returns a dictionary of all the data cleaned and ready for the
    schema to operate on.
    """
    
    def __init__(self, name: str):
        """
        Check if the folder exists
        Collects raw data, cleans it and logs any odd issues
        This would be when data we expect doenst exist 
        We will need to create a formal list for expected and valid field entries
        
        e.g.
        data science vs data scienc
        
        """
        if not VALID_NAME.match(name):
            raise ValueError(f"Invalid dataset name: {name!r}")
        self.name = name
        self.raw = {}
        self.major_codes = {}
        self.degree_codes = {}
        self.clean = {}  
        self.tables ={}      

    @property
    def data_dir(self) -> Path:
        return config.DATASETS_DIR / self.name

    @property
    def clean_file(self) -> Path:
        # In a subfolder so json_files() never loads it back in as input
        return self.data_dir / "parsed" / "clean.json"
    
    def json_files(self) -> list[Path]:
        return sorted(self.data_dir.glob("*.json"))

    # =========================
    # LOAD AND CHECK
    # =========================
    
    def load(self) -> dict:
        """
        This attempts every file in the current directory
        
        We work from "raw" 
        """
        for path in self.json_files():
            with path.open(encoding="utf-8") as f:
                self.raw[path.stem] = json.load(f)
        return self.raw
    
    # =========================
    # CLEANING
    # =========================
    def clean_degrees(self) -> dict:
        """
        For each degree apply the known issues and resolve each field 
        to a standardised format.
        """
        
        degrees = {}
        
        for code, r in self.raw["degrees"].items():
            study_type = STUDY_TYPES.get(code[:2])
            components = self.combined_components(r.get("title")) if study_type == "Combined" else []
    
            degrees[code] = {
                "code": code,
                "title": text(r.get("title")),
                "school": text(r.get("school")),
                "study_type": study_type,                                
                "total_points": number(r.get("total_points")),
                "duration_years": number(r.get("standard_full_time_completion")),
                "locations": text_list((r.get("locations") or "").split(",")), 
                "majors": text_list(r.get("majors")),
                "component_titles": components,
                "components": [self.degree_codes[t] for t in components if t in self.degree_codes],
            }
            
        return degrees

    def clean_majors(self) -> dict:
        """
        For each major apply the known issues and resolve each field 
        to a standardised format.
        """
        
        majors = {}
        
        for code, r in self.raw["majors"].items():
            
            # This is something i'm considering about handling.
            # Like a code could be tied to a school and a name somehow
            # but i haven't figured out. It tells us units exist somehow. 
            # But it would break our expected format to not have the basic objects.

            majors[code] = {
                "code": code,
                "title": text(r.get("title")),
                "school": text(r.get("school")),
                "description": text(r.get("description")),
                "outcomes": text_list(r.get("outcomes")),
                "degrees": text_list(r.get("courses")),     
                "bridging": text_list(r.get("bridging")),                       
                "units": text_list(r.get("units")),                             
            }
        return majors

    def clean_units(self) -> dict:
        """
        For each major apply the known issues and resolve each field 
        to a standardised format.
        """
        units = {}
        
        for code, r in self.raw["units"].items():
            
            raw_semesters = text_list(r.get("semesters"))
            major_titles = text_list(self.major_title(m) for m in r.get("majors") or [])
 
            units[code] = {
                "code": code,
                "title": text(r.get("title")),
                "school": text(r.get("school")),
                "level": number(r.get("level")),
                "credit": number(r.get("credit")),
                "description": text(r.get("description")),
                "available": not any(s in UNAVAILABLE for s in raw_semesters),
                "semesters": [s for s in raw_semesters if s not in UNAVAILABLE],
                "locations": text_list(r.get("locations")),
                "major_titles": major_titles, 
                "modes": text_list(r.get("modes")),
                "outcomes": text_list(r.get("outcomes")),
                "assessment": text_list(r.get("assessment")),
                # Need both clean text and number for every key value pair from the cotact items
                # This was a tough loop lol comments just to remind myself the goal.
                "major_codes": [self.major_codes[t] for t in major_titles if t in self.major_codes],
                "contact": {text(k): number(v) for k, v in (r.get("contact") or {}).items()},
                "prerequisites": text_list(flatten(r.get("prerequisite_units"))),                                 
                "prerequisite_degrees": text_list(r.get("prerequisite_courses")),
                "prerequisites_text": text(r.get("prerequisites_text")),
                "advisable_prior_study": text_list(r.get("advisable_prior_study")),
                "note": text(r.get("note")),
            }
        return units

    # =========================
    # Additional mapping objects
    # =========================
    def major_title(self, title):
        """
        Attempt to resolve when a title is missing it's last letter.
        In units this is an obvious issue and we hope to rectefy them automatically
        as I only know of 4/5 but could be more. 
        
        attempt to clean and use forced map typing. Find known major names
        and fix if its only one letter missing. Return the new title.
        """
        title = text(title)  

        known = set()
        for m in self.raw["majors"].values():
            known.add(text(m.get("title")))
            
        if title is None or title in known:
            return title
        
        matches = []
        for k in known:
            if k[:-1] == title:
                matches.append(k)

        if len(matches) == 1:
            return matches[0]
        else:
            return title
        
    def combined_components(self, title):
        """
        Use regular expression to split mutiple named things to singular form
        """
        return text_list(COMBINED_SPLIT.split(title or ""))
 

    # =========================
    # EVERYTHING
    # =========================
    def parse(self) -> dict:
        """
        Load the full dataset and return cleaned values ready for schema to use
        
        This also assumes that the dataset is available or will probably crash.
        IDGAF for extensive handling here lol. We know expectations.
        """
        self.load()
        
        self.major_codes = {text(m.get("title")): code for code, m in self.raw["majors"].items()}
        self.degree_codes = {text(d.get("title")): code for code, d in self.raw["degrees"].items()}
        
        self.clean = {
            "degrees": self.clean_degrees(),
            "majors": self.clean_majors(),
            "units": self.clean_units(),
        }
        return self.clean

