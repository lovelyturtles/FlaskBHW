from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

## TO DOS / COMMENTS
""" 
I'm not really sure how to change the url from displaying /views/path
Ideally don't want it to dispaly /views before the path 

Still need to retrieve the input from the user through a form and send for
find_a_doctor and send it to the /find_a_doctor/<location> path to display 
the recommendations for the corresponding zip 

 """

# Create a Flask Instance
app = Flask(__name__)

## routes 

# you can put arguments in the render_template so that these variables 
# can be accessed in the corresponding html template
# {{name}} <- to be rendered to the screen for example
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        zip_code = request.form.get("zip_code")
        print(zip_code)
    return render_template('index.html')

## initial page for the "find a doctor" tab that 
## takes in a form for the desired location 
## form should route to the located_doctors html based on the passed in arguments
@app.route("/find_a_doctor")
def doctor_locator(): 
    args = request.args
    location = args.get("zip")
    return render_template("find_a_doctor.html", zip = location)

## dynamic URL to route to a new HTML that displays the location's
# recommended doctors
@app.route("/find_a_doctor/<location>")
def doctor_located(location): 
    # name = args.get("name") <-- access query parameter example
    return render_template("located_doctors.html", place = location)

## renders the learn more page 
@app.route("/learn_more")
def learn_more(): 
    return render_template("learn_more.html")


if __name__ == "__main__":
    app.run(debug=True)

