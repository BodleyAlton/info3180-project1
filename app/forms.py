from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, PasswordField, SelectField, IntegerField
from wtforms.validators import InputRequired

class ProfileForm(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    age = IntegerField('Age', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[('male','Male'),('female','Female')])
    bio = TextAreaField('Biography', validators=[InputRequired()])
    profpic = FileField('Profile Image', validators=[InputRequired()])