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