#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, flash, url_for, redirect
from forms import SigninForm, SignupForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

"""Flask is a web framework to build web applications, developed by Armin Ronacher.
based on WSGI(Web Server Gateway Interface) toolkit and jinja template engine."""

app = Flask(__name__)
app.env = "development"
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # /// represents relative path in SQLite

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(40), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

@app.route("/")
@app.route("/home")  # sets both / and home to same function
def home():
    username = 'Sai'
    user = [{'name': 'Anand', 'content': 'Be Cool !!!'}, {'name': 'Raj', 'content': 'Chill Bro'}]
    # return '<h3>Hello, ' + user['username'] + '</h3>'
    return render_template('home.html', user=user, username=username)


@app.route("/register")
def register():
    form = SignupForm()
    return render_template('register.html', title='Sign Up', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = SigninForm()
    if form.validate_on_submit():
        flash('{} is logged in'.format(form.email.data))
        return redirect('/home')  # url_for('home'))  # can use return redirect('/login')
    return render_template('login.html', title='Sign in', form=form)


@app.route("/contact")
def contact():
    username = 'Sai'
    user = [{'fname': 'Sai', 'lname': 'Talluri'}, {'fname': 'Richard', 'lname': 'Green'}]
    # return '<h3>Hello, ' + user['username'] + '</h3>'
    return render_template('contact.html', users=user, username=username)


if __name__ == "__main__":  # to run the code directly without flask run
    app.run(debug=True)
