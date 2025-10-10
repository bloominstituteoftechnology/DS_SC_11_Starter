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
from dotenv import load_dotenv
import os

# Initialize Flask app
load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)

# Initialize OpenAQ API with your key
# TODO: Replace 'your_api_key_here' in the .env file with your actual OpenAQ API key
api = OpenAQ(key=os.getenv('OPEN_AQ_API_KEY'))


class Record(DB.Model):
    """Database model for storing air quality records."""
    # TODO: Complete the Record model with the following fields:
    # - id (integer, primary key)
    # - datetime (string)
    # - value (float, cannot be null)
    
    # TODO: Implement the __repr__ method for nice string representation
    pass


def get_results():
    """Get PM2.5 measurements using OpenAQ API v3 structure.
    
    TODO: Implement this function to:
    1. Get locations using api.locations()
    2. For each location, get sensors using api.sensors_by_location_id()
    3. For PM2.5 sensors, get measurements using api.measurements_by_sensor_id()
    4. Return a list of (datetime, value) tuples
    5. Include fallback sample data if no real data is available
    """
    # TODO: Implement the three-step API v3 process
    # Step 1: Get locations
    # Step 2: Get sensors for each location
    # Step 3: Get measurements for PM2.5 sensors
    
    # TODO: Add fallback sample data
    sample_data = [
        ('2024-01-01T00:00:00Z', 15.2),
        ('2024-01-01T01:00:00Z', 18.7),
        ('2024-01-01T02:00:00Z', 12.3),
        ('2024-01-01T03:00:00Z', 22.1),
        ('2024-01-01T04:00:00Z', 19.8)
    ]
    
    return sample_data  # TODO: Replace with actual implementation


@app.route('/')
def root():
    """Base view - displays filtered air quality data."""
    # TODO: Query database for records with value >= 18
    # TODO: Return the filtered records as a string
    return 'TODO - implement database filtering'


@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    # TODO: Drop all existing tables
    # TODO: Create new tables
    # TODO: Get data from get_results()
    # TODO: Create Record objects and add to database
    # TODO: Commit changes
    # TODO: Return the root view
    return 'TODO - implement data refresh'


if __name__ == '__main__':
    app.run(debug=True)
