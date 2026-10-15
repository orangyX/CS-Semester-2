from flask import render_template, Flask, request
from fake_data import FAKE_DEGREES, FAKE_MAJORS, FAKE_UNITS, FAKE_LOCATION_RESULTS, FAKE_SEARCH_RESULTS, FAKE_FOUNDATIONAL, FAKE_AVERAGE, FAKE_VIOLATIONS

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

@app.route("/validation")
def validation():
    return render_template("results.html", title="Data validation", columns=["Entity", "Problem", "Property"], rows=FAKE_VIOLATIONS) 
# Just reuse, since validation in this case will be in table form

@app.route("/query/location")
def location_query():
    location = request.args.get("location")
    rows = FAKE_LOCATION_RESULTS.get(location, [])

    return render_template("results.html", title=f"Majors available in {location}", columns=["Code", "Title"], rows=rows)

@app.route("/query/foundational")
def foundational_query():
    return render_template("results.html", title="Foundational units by degree", columns=["Degree", "Unit"], rows=FAKE_FOUNDATIONAL)

@app.route("/query/average-majors")
def average_query():
    return render_template("results.html", title="Average majors by degree", columns=["Degree type", "Average majors"], rows=FAKE_AVERAGE)

@app.route("/search")
def search():
    q = request.args.get("q") # Search box name is q
    rows = FAKE_SEARCH_RESULTS

    return render_template("results.html", title=f"Majors matching \"{q}\"", columns=["Code", "Title", "Matching outcome"], rows=rows)

if __name__ == "__main__":
    app.run(debug=True)