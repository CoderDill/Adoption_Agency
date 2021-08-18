from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired


class AddPetForm(FlaskForm):

    name = StringField("Pet name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")
