# -*- coding:utf-8 -*-

from flask import Blueprint, session, request
from flask import render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from database import db

from .forms import PostForm
from .models import Task

from customer.models import *
from contributor.models import *  

                

app = Blueprint('index', __name__, template_folder='templates')



@app.route("/")
def landing_page():
    return render_template('main/index.html')

@app.route("/services")
def services():
    if login() is True :return redirect(url_for('start.index'))
    return render_template('main/services.html')

@app.route("/prepare/<task_type>")
def prepare_job(task_type):
    if login() is True :return redirect(url_for('start.index'))
    if task_type == "transcription":
        return render_template('main/transcription.html')
    if task_type == "collection":
        return render_template("main/collection.html")    
    else: return render_template('main/services.html')     
    return render_template('main/services.html')

@app.route("/crowd", methods=['POST', 'GET'])
def crowd_selection():
    if login() is True :return redirect(url_for('start.index')) 
    session['task_data'] = request.form['task_data']
    return render_template('main/crowd.html', task_data=session['task_data'])

@app.route('/logout')
def logout():
    from start.views import index
    session.clear()
    return redirect(url_for('start.index'))

def login():
    if not 'customer_id' in session :
        from start.views import index
        flash('please login first')
        return True
    else :return False          
