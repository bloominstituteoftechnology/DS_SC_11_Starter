"""OpenAQ Air Quality Dashboard with Flask - Starter Template

This is a starter template for the Air Quality Dashboard Sprint Challenge.
Complete the TODO items to build a fully functional dashboard.

Setup Instructions:
1. Install dependencies: pip install flask flask-sqlalchemy requests py-openaq pytest
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from openaq import OpenAQ

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)
