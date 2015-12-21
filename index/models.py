# -*- coding:utf-8 -*-
from database import db
from datetime import datetime, date
from flask import url_for
from customer.models import *
from contributor.models import *

class Task(db.Model):
    __tablename__='tasks'
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime)
    task_name = db.Column(db.String(80))
    task_description = db.Column(db.String(240))
    task_criteria = db.Column(db.String(120))
    status = db.Column(db.Integer)
    delete = db.Column(db.Integer)
    form =  db.relationship('Form', backref='tasks')
    customer_id = db.Column(db.Integer , db.ForeignKey('customers.id'))
    
    def __init__(self, task_name, task_description, task_criteria, status,
                 cutomer_id, delete=0, create_date=date.today()):
        self.task_name = task_name
        self.task_description = task_description
        self.task_criteria = task_criteria
        self.status = status
        self.delete = delete
        self.customer_id = cutomer_id
        self.create_date = create_date

    def __repr__(self):
        return self.task_name


class Form(db.Model):
    __tablename__='forms'
    id = db.Column(db.Integer ,primary_key=True)
    label = db.Column(db.String(120))
    value = db.Column(db.Text)
    ftype = db.Column(db.Text)
    condition = db.Column(db.Text)
    require = db.Column(db.Text)
    task_id = db.Column(db.Integer , db.ForeignKey('tasks.id'))
    create_date = db.Column(db.DateTime)
    delete = db.Column(db.Integer)

    def __init__(self, label, value, ftype, condition, require, task_id, delete=0, create_date=date.today()):
        self.label = label
        self.value = value
        self.ftype = ftype
        self.condition = condition
        self.require = require
        self.task_id = task_id
        self.delete = delete
        self.create_date = create_date  



class ContributorTask(db.Model):
    __tablebname__='contributortasks'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    task_id = db.Column(db.Integer)
    contributor_id = db.Column(db.Integer , db.ForeignKey('contributors.id'))
    geo_code = db.Column(db.String)
    create_date = db.Column(db.DateTime)
    status = db.Column(db.String(8))
    delete = db.Column(db.Integer)

    def __init__(self, customer_id, task_id, contributor_id, status, delete=0, create_date=date.today()):
        self.customer_id = customer_id
        self.task_id = task_id
        self.contributor_id =contributor_id
        self.status = status
        self.delete = delete
        self.create_date = create_date
    

class Skill(db.Model):
    _tablebname__='skills'
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String)
    num_contributors = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    delete = db.Column(db.Integer)

    def __init__(self, skill, num_contributors,  delete=0, create_date=date.today()):
        self.skill = skill
        self.num_contributors = num_contributors
        self.create_date = create_date
        self.delete = delete