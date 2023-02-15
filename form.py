from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf, Length


class AddPetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField("Pet name", validators=[
                        InputRequired(message="Pet name can't be empty.")])
    species = StringField("Species", validators=[
                        InputRequired(message="Species can't be empty."),
                        AnyOf(["cat","dog","porcupine"], message="The species should be either 'cat', 'dog', or 'porcupine'")])
    photo_url = StringField("Photo URL", validators=[Optional(),URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0,max=30,message="The age should be between 0 and 30")])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")