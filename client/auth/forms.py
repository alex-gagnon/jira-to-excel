from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import StringField, SubmitField, BooleanField


class Auth(FlaskForm):
    username = StringField(label='Username',
                           validators=[validators.DataRequired()])
    password = StringField(label='Password',
                           validators=[validators.DataRequired()])
    remember = BooleanField(label='Remember me',
                            validators=[validators.Optional()])
    login = SubmitField(label='Login')
    signup = SubmitField(label='Signup')
