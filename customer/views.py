# -*- coding:utf-8 -*-

from flask import Blueprint, request, session
from flask import render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from database import db
from .models import Customer
from index.models import ContributorTask, Task
from forms import LoginForm as CustomerLogin
from forms import ProfileForm

app = Blueprint('customer', __name__, template_folder='templates')


# client controller

# @app.route('/jobs/<delete>')
@app.route('/jobs/')
def list_jobs(delete=None):
    if login() is True: return redirect(url_for('start.index'))
    customer = Customer.query.get(session['customer_id'])
    customer_task = customer.task
    if request.args.get('delete'):
        task_id = - int(request.args.get('delete'))
        customer_task[task_id].delete = 1
        try:
            db.session.commit()
        except:
            flash("couldnt delete")
    return render_template('customer/list_jobs.html', delete=delete, customer_task=customer_task)


@app.route('/profile')
def profile():
    if login() is True: return redirect(url_for('start.index'))
    customer = Customer.query.get(session['customer_id'])
    profileform = ProfileForm()
    # upate profile
    if request.form:
        form = ProfileForm(request.form)
        if request.method == 'POST' and form.validate():

            update = Customer(
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
    if login() is True: return redirect(url_for('start.index'))
    task_id = int(request.args.get('task_id'))
    contributors = ContributorTask.query.filter_by(task_id=task_id)
    task = Task.query.get(task_id)
    customer_task = task
    contributions = []
    complete_contributions = []
    active_contributions = []
    for contributor in contributors:
        count = + 1
        contributions.append(contributor)
        if contributor.status == 0:
            complete_contributions.append(contributor)
        else:
            active_contributions.append(contributor)

        """  
        present_contributors
        contributors
        completion_time
        amount_spent
        amount_left 
        failed_test"""
        num_contributors = count
        per_complete = (len(complete_contributions) / float(count)) * 100
    return render_template('customer/dashboard.html', task_id=task_id,
                           complete_contributions=complete_contributions,
                           active_contributions=active_contributions,
                           num_contributors=num_contributors,
                           per_complete=per_complete,
                           num_active_contributions=
                           len(active_contributions),
                           num_complete_contiributions=
                           len(complete_contributions),
                           customer_task=customer_task)


@app.route('/payment')
def payment():
    if login() is True: return redirect(url_for('start.index'))
    return render_template('customer/dashboard.html')


@app.route('/customerlogin', methods=['GET', 'POST'])
def customerlogin():
    customerlogin = CustomerLogin()
    if request.form:
        form = CustomerLogin(request.form)
        if request.method == 'POST' and form.validate():
            customer = Customer.query.filter_by(email=form.email.data.lower()).first()

            if customer:
                if form.password.data == customer.password:
                    session['customer_id'] = customer.id
                    flash('login succesfully')
                    return redirect(url_for('customer.list_jobs'))

    flash('login faild')
    return render_template('index.html', customerlogin=customerlogin)

    # check if customer is loggedin


def login():
    if not 'customer_id' in session:

        flash('please login first')
        return True
    else:
        return False
