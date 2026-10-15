FAKE_DEGREES = {
    "BP001": {
        "code": "BP001", "title": "Bachelor of Arts", "study_type": "Bachelor",
        "points": 144,
        "majors": [
            {"code": "MJD_CMPSCX", "title": "Linear Algebra"},
        ],
    },
    "BP004": {
        "code": "BP004", "title": "Bachelor of Science", "study_type": "Bachelor",
        "points": 144,
        "majors": [
            {"code": "MJD_CMPSCI", "title": "Computer Science"},
            {"code": "MJD_CMPSCX", "title": "Linear Algebra"},
        ],
    },
}

FAKE_MAJORS = {
    "MJD_CMPSCI": {
        "code": "MJD_CMPSCI",
        "title": "Computer Science",
        "school": "School of Physics, Mathematics and Computing",
        "units": [
            {"code": "CITS1401", "title": "Computational Thinking with Python", "level": 1, "credit": 6},
            {"code": "CITS2200", "title": "Data Structures and Algorithms", "level": 2, "credit": 6},
            {"code": "CITS3005", "title": "Knowledge Representation", "level": 3, "credit": 6},
        ],
    },
    "MJD_CMPSCX": {
        "code": "MJD_CMPSCX",
        "title": "Linear Algebra",
        "school": "School of Physics, Mathematics and Computing",
        "units": [
            {"code": "MATH1011", "title": "Multivariable Calculus", "level": 1, "credit": 6},
            {"code": "MATH1012", "title": "Mathematical Theory and Methods", "level": 1, "credit": 6},
        ],
    },
}

FAKE_UNITS = {
    "CITS1401": {
        "code": "CITS1401", "title": "Computational Thinking with Python",
        "level": 1, "credit": 6,
        "direct_prereqs": [],
        "all_prereqs": [],
    },
    "CITS2200": {
        "code": "CITS2200", "title": "Data Structures and Algorithms",
        "level": 2, "credit": 6,
        "direct_prereqs": [{"code": "CITS1401", "title": "Computational Thinking with Python"}],
        "all_prereqs":    [{"code": "CITS1401", "title": "Computational Thinking with Python"}],
    },
    "CITS2211": {
        "code": "CITS2211", "title": "Discrete Structures",
        "level": 2, "credit": 6,
        "direct_prereqs": [{"code": "MATH1012", "title": "Mathematical Theory and Methods"}],
        "all_prereqs":    [{"code": "MATH1012", "title": "Mathematical Theory and Methods"},
                           {"code": "MATH1011", "title": "Multivariable Calculus"}],
    },
    "CITS3005": {
        "code": "CITS3005", "title": "Knowledge Representation",
        "level": 3, "credit": 6,
        "direct_prereqs": [{"code": "CITS2200", "title": "Data Structures and Algorithms"},
                           {"code": "CITS2211", "title": "Discrete Structures"}],
        "all_prereqs":    [{"code": "CITS2200", "title": "Data Structures and Algorithms"},
                           {"code": "CITS2211", "title": "Discrete Structures"},
                           {"code": "CITS1401", "title": "Computational Thinking with Python"},
                           {"code": "MATH1012", "title": "Mathematical Theory and Methods"},
                           {"code": "MATH1011", "title": "Multivariable Calculus"}],
    },
    "MATH1011": {
        "code": "MATH1011", "title": "Multivariable Calculus",
        "level": 1, "credit": 6,
        "direct_prereqs": [],
        "all_prereqs": [],
    },
    "MATH1012": {
        "code": "MATH1012", "title": "Mathematical Theory and Methods",
        "level": 1, "credit": 6,
        "direct_prereqs": [{"code": "MATH1011", "title": "Multivariable Calculus"}],
        "all_prereqs":    [{"code": "MATH1011", "title": "Multivariable Calculus"}],
    },
}

FAKE_LOCATION_RESULTS = {
    "Albany":   [["MJD-ANTHR", "Anthropology"], ["MJD-HISTY", "History"]],
    "UWAPerth": [["MJD-CMPSC", "Computer Science"], ["MJD-ESOFT", "Software Engineering"]],
}

FAKE_SEARCH_RESULTS = [
    ["MJD-CMPSC", "Computer Science", "apply data analysis techniques to …"],
    ["MJD-DATSC", "Data Science", "perform data analysis and visualisation …"],
]   

FAKE_FOUNDATIONAL = [
    ["BP004", "SCIE1104"],
    ["BH011", "GENG1000"],
]

FAKE_AVERAGE = [
    ["Bachelor", "21.3"], 
    ["Combined", "9.3"], 
    ["Honours", "6.5"]
]

FAKE_VIOLATIONS = [
    ["MUSC2751", "Unit is its own prerequisite", "unitHasPrerequisite"],
    ["MUSC3751", "Unit is its own prerequisite", "unitHasPrerequisite"],
    ["BH005", "Degree has no major (before reasoning)", "degreeHasMajor"],
]