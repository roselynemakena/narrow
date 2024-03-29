# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template

app = Blueprint('contributor', __name__, template_folder='templates')


# client controller

@app.route('/jobs')
def list_jobs():
    return render_template('contributor/list_jobs.html')


@app.route('/profile')
def profile():
    return render_template('contributor/profile.html')


@app.route('/dashboard')
def dashboard():
    return render_template('contributor/dashboard.html')


@app.route('/payment')
def payment():
    return render_template('contributor/dashboard.html')
