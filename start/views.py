# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from database import db


app = Blueprint('start', __name__, template_folder='templates')



@app.route("/")
def index():
    return render_template('index.html')
