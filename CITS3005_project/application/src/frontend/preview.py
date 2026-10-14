from flask import render_template, Flask
from fake_data import FAKE_DEGREES, FAKE_MAJORS, FAKE_UNITS

app = Flask(__name__) # Create app

@app.route('/degrees')
def degrees():
    return render_template("lists/degrees.html", degrees=list(FAKE_DEGREES.values()))

@app.route("/majors")
def majors():
    return render_template("lists/majors.html", majors=list(FAKE_MAJORS.values()))

@app.route("/units")
def units():
    return render_template("lists/units.html", units=list(FAKE_UNITS.values()))

@app.route("/degree/<code>")
def degree_details(code):
    degree = FAKE_DEGREES.get(code)
    
    return render_template("details/degree.html", degree=degree)

@app.route("/major/<code>")
def major_details(code):
    major = FAKE_MAJORS.get(code)
    
    return render_template("details/major.html", major=major)

@app.route("/unit/<code>")
def unit_details(code):
    unit = FAKE_UNITS.get(code)
    
    return render_template("details/unit.html", unit=unit)

@app.route('/') # Route to home address
def home():
    return render_template('home.html')

@app.route("/queries")
def queries():
    return render_template("queries.html")

if __name__ == "__main__":
    app.run(debug=True)