# -*- coding:utf-8 -*-

from flask import Blueprint, request
from flask import render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from database import db

from .models import Customer

from forms import LoginForm as CustomerLogin

app = Blueprint('customer', __name__, template_folder='templates')

#client controller 

@app.route('/jobs')
def list_jobs():
    return render_template('customer/list_jobs.html')

@app.route('/profile')
def profile():
    return render_template('customer/profile.html')

@app.route('/dashboard')
def dashboard():
    return render_template('customer/dashboard.html')


@app.route('/payment')
def payment():
    return render_template('customer/dashboard.html')
   
@app.route('/customerlogin', methods=['GET', 'POST'])
def customerlogin():
    customerlogin = CustomerLogin()
    if request.form :
        form =CustomerLogin(request.form)
        if request.method == 'POST' and form.validate():
            
            flash('login succesful')
            return redirect(url_for('customer.list_jobs'))
    flash('login falied')    
    return render_template('index.html', customerlogin=customerlogin)     


