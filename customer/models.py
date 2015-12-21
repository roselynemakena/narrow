# -*- coding:utf-8 -*-
from database import db
from datetime import datetime, date
from flask import url_for
        
#Customer Model

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email  = db.Column(db.String(120))
    password = db.Column(db.String(400)) 
    delete = db.Column(db.Integer)
    task = db.relationship('Task', backref='customers')
    

    
    def __init__(self, first_name,last_name, email, password, delete=0, create_date=date.today()):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.create_date = create_date
        self.delete =delete
    
    def __repr__(self):
        return self.first_name          

