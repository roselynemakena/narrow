# -*- coding:utf-8 -*-

from flask import Blueprint, request, session
from flask import render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from database import db
from .models import Customer

from forms import LoginForm as CustomerLogin
from forms import ProfileForm 

app = Blueprint('customer', __name__, template_folder='templates')

#client controller 

@app.route('/jobs')
def list_jobs():
    if login() is True :return redirect(url_for('start.index'))
    customer = Customer.query.get(session['customer_id'])   
    customer_task = customer.task
    return render_template('customer/list_jobs.html', customer_task = customer_task)

@app.route('/profile')
def profile():
    if login() is True :return redirect(url_for('start.index'))
    customer = Customer.query.get(session['customer_id']) 
    profileform = ProfileForm()
    #upate profile
    if request.form :
        form = ProfileForm(request.form)
        if request.method == 'POST' and form.validate():

            update= Customer(
                form.first_name.data,
                form.last_name.data,
                form.email.data,
                form.password.data
                )

           
            if db.session.commit(update):
                    flash("Profile updates succesfully")
    return render_template('customer/profile.html', customer=customer,
        profileform=profileform)

@app.route('/dashboard')
def dashboard():
    if login() is True :return redirect(url_for('start.index'))
    return render_template('customer/dashboard.html')


@app.route('/payment')
def payment():
    if login() is True :return redirect(url_for('start.index'))
    return render_template('customer/dashboard.html')
   
@app.route('/customerlogin', methods=['GET', 'POST'])
def customerlogin():
    customerlogin = CustomerLogin()
    if request.form :
        form = CustomerLogin(request.form)
        if request.method == 'POST' and form.validate():
           customer = Customer.query.filter_by(email = form.email.data.lower()).first()
           
           if customer :
               if form.password.data == customer.password:
                   session['customer_id'] = customer.id
                   customer_task = customer.task
                 
                   flash('login succesfully')
                   return redirect(url_for('customer.list_jobs'))

    flash('login faild')    
    return render_template('index.html', customerlogin=customerlogin)   

 #check if customer is loggedin     
def login():
    if not 'customer_id' in session :
        from start.views import index
        flash('please login first')
        return True
    else :return False     

