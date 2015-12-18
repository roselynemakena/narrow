# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from database import db

from customer.models import *
from index.models import *
from contributor.models import *


app = Blueprint('start', __name__, template_folder='templates')



@app.route("/")
def index():
		
		# create a customer with task  
		customer_one = Customer("edmond", "mensah", "primerossgh@gmail.com", "password")
		print "************************************************************************"
		print customer_one.id
		db.session.add(customer_one)
		db.session.commit()

		task = Task("app survey", "survey of the slydepay app", "english,tech survey", "active" ,customer_one.id)
		db.session.add(task)
		db.session.commit()

		feild_one = Form("do you like the background?", "yes", "testfield", "", "", task.id)
		feild_two = Form("is the sidebar too big?", "yes", "testfield", "", "", task.id)

		db.session.add_all([feild_one, feild_two])
		db.session.commit()
        
		contributor_one = Contributor("charles", "andor", "kwasiamantin@gmail.com", "password", "{english:high,french:low}")

		db.session.add(contributor_one)
		db.session.commit()
		
		current_task = ContributorTask(customer_one.id, task.id, contributor_one.id, "active") 

		db.session.add(current_task)
		db.session.commit()
		cont = contributor_one.contributor_task

		for a in cont :
			print "************************"
			print a.customer_id


		#get all task related to a customer 
		task = Task.query.filter_by(id=1).first()   
		for field in task.form :
		   	print field.label
		        

		return render_template('index.html')

