#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template

"""Flask is a web framework to build web applications, developed by Armin Ronacher.
based on WSGI(Web Server Gateway Interface) toolkit and jinja template engine."""

app = Flask(__name__)


@app.route("/")
@app.route("/home")    #sets both / and home to same function
def hello():
	username = 'Sai'
	user = [{'name': 'Anand', 'content': 'Be Cool !!!'}, {'name': 'Raj', 'content': 'Chill Bro'}]
	# return '<h3>Hello, ' + user['username'] + '</h3>'
	return render_template('home.html', user=user,username = username)


@app.route("/contact")
def contact():
	username = 'Sai'
	user = [{'fname':'Sai','lname':'Talluri'},{'fname':'Richard','lname':'Green'}]
	#return '<h3>Hello, ' + user['username'] + '</h3>'
	return render_template('contact.html',users = user,username = username)


if __name__ == "__main__":     # to run the code directly without flask run
	app.run(debug=True)




