from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Optional


class LoginForm(FlaskForm):
    email = StringField('Email',)
    username = StringField('Username',)
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Optional()])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    register = SubmitField('Register')

    def validate_username(self, username):
        pass
