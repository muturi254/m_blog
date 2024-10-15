import sqlalchemy as sa
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import db
from app.models import User


# class forms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # validate username
    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))

        if user is not None:
            raise ValidationError("Username already taken, use a different one")
        
    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))

        if user is not None:
            raise ValidationError("Email already in use, try a different one")