from flask import render_template, Flask
from fake_data import FAKE_DEGREES, FAKE_MAJORS

app = Flask(__name__) # Create app

@app.route('/degrees')
def degrees():
    # Build fake degrees here and test degrees.html
    art = {"code": "BP001", "title": "Bachelor of Arts", "study_type": "Bachelor"}
    science = {"code": "BP004", "title": "Bachelor of Science", "study_type": "Bachelor"}

    deg_list = [art, science]

    return render_template("lists/degrees.html", degrees=deg_list)

@app.route("/units")
def units():
    # Build fake units
    cits1401 = {"code": "CITS1401", "title": "Computational thinking with Python", "level": 1, "credits": 6}
    evilCits1401 = {"code": "CITS1403", "title": "Computational thinking with C++", "level": 1, "credits": 6}
    
    unit_list = [cits1401, evilCits1401]
    
    return render_template("lists/units.html", units=unit_list)

@app.route("/majors")
def majors():
    # Build fake majors
    cmp_sci = {"code": "MJD_CMPSCI", "title": "Computer Science", "school": "School of Physics, Mathematics and Computing"}
    evil_cmp_sci = {"code": "MJD_CMPSCX", "title": "Linear Algebra", "school": "School of Physics, Mathematics and Computing"}
    
    major_list = [cmp_sci, evil_cmp_sci]
    
    return render_template("lists/majors.html", majors=major_list)

@app.route("/degree/<code>")
def degree_details(code):
    degree = FAKE_DEGREES.get(code)
    
    return render_template("details/degree.html", degree=degree)

@app.route("/major/<code>")
def major_details(code):
    major = FAKE_MAJORS.get(code)
    
    return render_template("details/major.html", major=major)

@app.route('/') # Route to home address
def home():
    return render_template('home.html')

@app.route("/queries")
def queries():
    return render_template("queries.html")

if __name__ == "__main__":
    app.run(debug=True)