# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from database import db

from .forms import PostForm
#from .models import Admin

app = Blueprint('index', __name__, template_folder='templates')



@app.route("/")
def landing_page():
    return render_template('main/index.html')

@app.route("/services")
def services():
    return render_template('main/services.html')

@app.route("/prepare")
def prepare_job():
    return render_template('main/prepare.html')

@app.route("/crowd")
def crowd_selection():  
    return render_template('main/crowd.html')
