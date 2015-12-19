# coding:utf-8

from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms import validators
from wtforms.fields.html5 import EmailField

class LoginForm(Form):
   email = EmailField('Email address', [validators.DataRequired(), validators.Email()])    
   password = PasswordField('Password', [validators.DataRequired()])
    

class ProfileForm(Form):
   email = EmailField('Email address', [validators.DataRequired(), validators.Email()])    
   password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
   ])
   confirm = PasswordField('Repeat Password')
   password_old = PasswordField('Old Password', [validators.DataRequired()])
   first_name = TextField('First Name', [validators.DataRequired()])
   last_name = TextField('Last Name', [validators.DataRequired()])
   
