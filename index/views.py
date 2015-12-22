# -*- coding:utf-8 -*-

from flask import Blueprint, session, request
from flask import render_template, flash, redirect
from contributor.models import *
from index.models import Skill
from database import db
from flask.ext.sandboy import Sandboy

app = Blueprint('index', __name__, template_folder='templates')


@app.route("/")
def landing_page():
    return render_template('main/index.html')


@app.route("/services")
def services():
    if login() is True: return redirect(url_for('start.index'))
    return render_template('main/services.html')


@app.route("/prepare/<task_type>")
def prepare_job(task_type):
    if login() is True: return redirect(url_for('start.index'))
    if task_type == "transcription":
        return render_template('main/transcription.html')
    if task_type == "collection":
        return render_template("main/collection.html")

    else:
        return render_template('main/services.html')
    return render_template("main/services.html")


@app.route("/taskdata", methods=['POST', 'GET'])
def task_data():
    if login() is True: return redirect(url_for('start.index'))
    session['task_data'] = request.form['task_data']
    print session['task_data']
    return session['task_data']


@app.route("/crowd")
def crowd_selection():
    skills = db.session.query(Skill)
    contributors = db.session.query(Contributor)
    num_contributors = contributors.count()
    task_data = session['task_data']
    session['task_data'] = ""
    return render_template('main/crowd.html', task_data=task_data,
                           skills=skills, contributors=contributors, num_contributors=num_contributors)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('start.index'))


def login():
    if not 'customer_id' in session:
        flash('please login first')
        return True
    else:
        return False
