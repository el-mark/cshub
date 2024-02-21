from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo,NumberRange


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min = 5, max= 20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password',message='The password must be the same')])
    date_of_birth = DateField('Date of Birth',validators=[DataRequired()])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')