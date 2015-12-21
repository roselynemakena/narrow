# -*- coding:utf-8 -*-
from database import db
from datetime import datetime, date
from flask import url_for


class Contributor(db.Model):
    __tablename__='contributors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    skill_rating = db.Column(db.Text)
    create_date = db.Column(db.DateTime)
    delete = db.Column(db.Integer)
    contributor_task = db.relationship('ContributorTask', backref='contributors')

    def __init__(self, first_name, last_name, email, password, skill_rating, delete=0, 
        create_date=date.today()):
                self.first_name = first_name
                self.last_name = last_name
                self.email = email
                self.password = password
                self.skill_rating = skill_rating
                self.delete = delete 
                create_date = create_date

          