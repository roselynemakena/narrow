# coding:utf-8

from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired


class PostForm(Form):
    name = TextField('name', validators=[DataRequired()])
    content =TextField('content',validators=[DataRequired()])