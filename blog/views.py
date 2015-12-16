# -*- coding:utf-8 -*-

from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from database import db

from .forms import PostForm
from .models import Admin

app = Blueprint('blog', __name__, template_folder='templates')

@app.route("/")
def list_posts_view():
    admins = Admin.query.all()
    return render_template('index.html', admins=admins)

@app.route("/add/", methods=['get', 'post'])
def add_post_view():
    form = PostForm()

    if form.validate_on_submit():
        try:
            obj = Admin(
                form.name.data,
                form.content.data
                )
            print form.content.data
            db.session.add(obj)
            db.session.commit()
            flash('Post add successfully')
            return redirect(url_for('blog.list_posts_view'))
        except IntegrityError, err:
            flash('There is already a post with that title. Please, try another.')

    return render_template('blog/add_post.html', form=form)

@app.route("/<slug>/")
def post_view(slug):
    admin = Admin.query.filter_by(slug=slug).first()
    return render_template('blog/post.html', admin=admin)