# Air Quality Dashboard Sprint Challenge

## Overview

Build a Flask-powered web application that displays air quality data from the OpenAQ API v3. The dashboard will store data in a SQLite database and filter for potentially risky PM2.5 levels.

## Quick Start

### 1. Setup Environment

```bash
# Install dependencies
pip install flask flask-sqlalchemy requests py-openaq pytest

# Or use pipenv
pipenv install flask flask-sqlalchemy requests py-openaq pytest
```

### 2. Get API Key

1. Visit [OpenAQ API Key page](https://docs.openaq.org/using-the-api/api-key)
2. Sign up for a free account
3. Generate an API key

### 3. Download Required Files

- Download `openaq.py` from the course materials
- Place it in your project directory

### 4. Start Coding

- Use `starter.py` as your starting point
- Follow the step-by-step instructions in the assignment
- Complete all TODO items

## Project Structure

```bash
your-project/
├── aq_dashboard.py         # Your completed solution
├── openaq.py               # OpenAQ API wrapper (download from course)
├── test_aq_dashboard.py    # Test file
├── requirements.txt        # Dependencies
└── db.sqlite3              # SQLite database (created automatically)
```

## Key Features to Implement

### Part 1: Flask Setup

- Basic Flask application
- Database configuration
- API initialization

### Part 2: OpenAQ API v3 Integration

- Three-step data retrieval process:
  1. Get locations: `api.locations()`
  2. Get sensors: `api.sensors_by_location_id(location_id)`
  3. Get measurements: `api.measurements_by_sensor_id(sensor_id)`
- Handle API rate limits and data availability
- Implement fallback sample data

### Part 3: Database Integration

- Create `Record` model with id, datetime, value fields
- Implement `/refresh` route to pull and store data
- Add proper `__repr__` method

### Part 4: Dashboard Filtering

- Filter records with `value >= 18` (potentially risky PM2.5 levels)
- Display filtered results on main page

## API v3 Changes (January 2025)

- **API Key Required**: Authentication via `X-API-Key` header
- **No Direct Measurements**: Must use locations → sensors → measurements flow
- **Rate Limiting**: Stricter limits, 429 errors common
- **Data Availability**: Many sensors lack recent measurements

## Testing

```bash
# Run tests
python -m pytest test_aq_dashboard.py -v

# Expected output: 4 tests passing
```

## Running the Application

```bash
# Method 1: Direct Python execution
python aq_dashboard.py

# Method 2: Flask CLI
FLASK_APP=aq_dashboard.py flask run
```

Visit `http://localhost:5000` to see your dashboard!

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install missing dependencies
2. **API Key Errors**: Ensure you have a valid OpenAQ API key
3. **Rate Limiting**: API v3 has strict limits - use fallback data
4. **No Data**: Many sensors don't have recent measurements

### Debug Tips

- Enable Flask debug mode: `app.run(debug=True)`
- Check API responses with print statements
- Use sample data when API is unavailable
- Test database operations in Flask shell

## Success Criteria

- [ ] Flask app runs without errors
- [ ] API key authentication works
- [ ] Database stores air quality data
- [ ] Dashboard filters for risky PM2.5 levels (≥18 μg/m³)
- [ ] All tests pass
- [ ] Handles API rate limits gracefully

## Stretch Goals (Optional)

- Add HTML templates for better UI
- Implement data visualization
- Add location-specific filtering
- Deploy to Heroku
- Add data science analysis (averages, trends)

Good luck! 🚀
