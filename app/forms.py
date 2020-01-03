from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    filmname = StringField('Enter film name: (use ; to separate multiple film names)', validators=[DataRequired()])
    submit = SubmitField('Search Netflix PT')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField("Who's watching?", validators=[DataRequired()])
    submit = SubmitField('Login to Netflix PT')    

class LogoutForm(FlaskForm):
    submit = SubmitField('Logout from Netflix PT')