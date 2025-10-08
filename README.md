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

<!-- outline flask setup -->

### Part 2: OpenAQ API v3 Integration

<!-- outline api v3 integration -->

### Part 3: Database Integration

<!-- add database integration -->

### Part 4: Dashboard Filtering

<!-- add dashboard filtering -->

## API v3 Changes (January 2025)

<!-- outline api v3 changes -->

## Testing

```bash
# Run tests
python -m pytest test_aq_dashboard.py -v

# Expected output: 4 tests passing
```

## Running the Application

```bash
# Python execution
```

<!-- visit localhost:5000 to see your dashboard -->

## Troubleshooting

### Common Issues

<!-- add common issues -->

### Debug Tips

<!-- add debug tips -->

## Success Criteria

<!-- add success criteria -->

## Stretch Goals (Optional)

<!-- add stretch goals -->

Good luck! 🚀
