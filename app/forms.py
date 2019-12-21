from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    filmname = StringField('Enter film name: ', validators=[DataRequired()])
    submit = SubmitField('Search Netflix PT')