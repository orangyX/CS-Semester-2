from flask import render_template, Flask

app = Flask(__name__) # Create app

@app.route('/degrees')
def degrees():
    # Build fake degrees here and test degrees.html
    art = {"code": "BP001", "title": "Bachelor of Arts", "study_type": "Bachelor"}
    science = {"code": "BP004", "title": "Bachelor of Science", "study_type": "Bachelor"}

    deg_list = [art, science]

    return render_template("degrees.html", degrees=deg_list)
    pass

@app.route('/') # Route to home address
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)