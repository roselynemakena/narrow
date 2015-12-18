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
    contributor_task = db.relationship('ContributorTask', backref='contributors')

    def __init__(self, first_name, last_name, email, password, skill_rating, create_date=date.today()):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        skill_rating = skill_rating
        create_date = create_date

  