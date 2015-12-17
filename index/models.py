# -*- coding:utf-8 -*-
from database import db
from datetime import datetime
from flask import url_for

"""
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime)
    name = db.Column(db.String(120))
    content_id = db.Column(db.Integer , 
        db.ForeignKey('content.id'))
    content = db.relationship('Content',
        backref = db.backref('admin',lazy='dynamic'))
    
    def __init__(self, name, content, create_date=None):
        self.name = name
        print content
        #self.content = content
    
    def __repr__(self):
        return self.name

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime)
    content = db.Column(db.String(120))
    
    def __init__(self, content, create_date=None):
         self.content = content

    def __repr__(self):
        return self.Content    

"""