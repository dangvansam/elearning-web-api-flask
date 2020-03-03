import numpy as np
from flask import Flask, request, render_template, url_for
import os
import sys

app = Flask(__name__)
@app.route('/index')
def index():
	return render_template('index.html')
@app.route('/')
def home():
	return render_template('index.html')
@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/courses')
def courses():
	return render_template('courses.html')
@app.route('/course')
def course():
	return render_template('course.html')
@app.route('/teachers')
def teachers():
	return render_template('teachers.html')
@app.route('/teacher')
def teacher():
	return render_template('teacher.html')
@app.route('/contact')
def contact():
	return render_template('contact.html')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        #print('login get')
    	return render_template('login.html')
    else:
        print(request.method)
        print('login post')
        print(request.form.get('inputName'))
        print(request.form.get('inputPassword'))
        return render_template('index.html')
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'GET':
    	return render_template('signup.html')
    elif request.method == 'POST':
        #xu ly so sanh json
        return render_template('index.html')
# @app.route('/home')
# def index():
# 	return render_template('index.html')
# @app.route('/home')
# def index():
# 	return render_template('index.html')
# @app.route('/home')
# def index():
# 	return render_template('index.html')
# @app.route('/home')
# def index():
# 	return render_template('index.html')

if __name__ == '__main__':
    #load_model()  # load model at the beginning once only
    app.run(debug=True)