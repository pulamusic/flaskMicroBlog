#!/usr/bin/env python3

import os

from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# SECRET_KEY generated through the python interpreter
# Check out just before this: https://youtu.be/UIJKdCIEXUQ?t=705
app.config['SECRET_KEY'] = '37d456110c111dbf6ac55f19113fadf4'

# some dummy data for setting up templates. This will be deleted at some point.
posts = [
    {
        'author': 'Jim Carroll',
        'title': 'Blog Post 1',
        'content': 'First post content: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted': 'September 20, 2019'
    },
    {
        'author': 'James G. Carroll',
        'title': 'Blog Post 2',
        'content': 'Second post content: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'date_posted': 'September 21, 2019'
    }
]

# Routes =========================

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# main conditional ============================

if __name__ == "__main__":
    app.run(debug=True)
