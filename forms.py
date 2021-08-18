from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, URL, Optional, AnyOf, NumberRange


class AddPetForm(FlaskForm):

    name = StringField("Pet name", validators=[])
    species = StringField("Species", validators=[
                          InputRequired(), AnyOf(['dog', 'cat', 'porcupine'], message="Must be a dog, cat or porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(
    )], default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvGEH8NRyLvs04jLQU7OObBBpZ_c7bw7TbbQ&usqp=CAU")
    age = IntegerField(
        "Age", [NumberRange(min=0, max=30, message="- Age cannot be above 30")])
    notes = StringField("Notes")
