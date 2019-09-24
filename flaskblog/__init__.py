#!/usr/bin/env python3

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# SECRET_KEY generated through the python interpreter
# Check out just before this: https://youtu.be/UIJKdCIEXUQ?t=705
app.config['SECRET_KEY'] = '37d456110c111dbf6ac55f19113fadf4'

# sqlite db for development. Will switch to PostgreSQL db for production.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
