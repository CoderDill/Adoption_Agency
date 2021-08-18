from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "adopt_me"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def show_pets():
    pets = Pet.query.all()
    return render_template("/show_pets.html", pets=pets)


@app.route("/add")
def show_pets():
    form = AddPetForm()

    if form.validate_on_submit():
        # name = form.name.data
        # species = form.species.data
        # photo_url = form.photo_url.data
        # age = form.age.data
        # notes = form.notes.data
        return redirect("/")
    else:
        return render_template("/.html")
