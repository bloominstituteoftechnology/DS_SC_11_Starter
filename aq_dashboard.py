"""OpenAQ Air Quality Dashboard with Flask - Starter Template

This is a starter template for the Air Quality Dashboard Sprint Challenge.
Complete the TODO items to build a fully functional dashboard.

Setup Instructions:
1. Install dependencies: pip install flask flask-sqlalchemy requests py-openaq pytest
2. Get a free API key from https://docs.openaq.org/using-the-api/api-key
3. Replace 'your_api_key_here' with your actual API key
4. Download the openaq.py file and place it in your project directory
5. Run the application: python starter.py
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from openaq import OpenAQ

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)

# Initialize OpenAQ API with your key
# TODO: Replace 'your_api_key_here' with your actual OpenAQ API key
api = OpenAQ(key='your_api_key_here')


