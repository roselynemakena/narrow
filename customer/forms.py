# coding:utf-8

from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms import validators
from wtforms.fields.html5 import EmailField

class LoginForm(Form):
   email = EmailField('Email address', [validators.DataRequired(), validators.Email()])    
   password = PasswordField('Password', [validators.DataRequired()])
    


