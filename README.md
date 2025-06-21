# Pokemon API

A Flask-based REST API for managing Pokemon data with capture functionality and icon retrieval.

## Features

- **Pokemon List**: Get paginated list of Pokemon with filtering and sorting options
- **Capture System**: Toggle Pokemon capture status
- **Captured Pokemon**: View all captured Pokemon
- **Icon URLs**: Get Pokemon icon URLs from external source
- **CORS Support**: Cross-origin resource sharing enabled

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning from GitHub)

## Installation

### Step 1: Get the Project from GitHub

**Clone from GitHub**
```bash
# Clone the repository
git clone https://github.com/OhadB16/pokedex.git

# Navigate to the project directory
cd pokedex
```


### Step 2: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- Flask==2.0.2
- flask-cors==3.0.10
- werkzeug==2.2.3


## Running the Application

### Step 4: Start the Server

You have two options to run the application:

**Using run.py**
```bash
python run.py
```


The server will start on port 8080. You should see output similar to:
```
 * Running on http://127.0.0.1:8080
 * Debug mode: off
```

### Step 5: Access the Application

Open your web browser or use a tool like curl to access the API:

- **Base URL**: http://localhost:8080
- **Health Check**: http://localhost:8080/

## API Endpoints

### 1. Get Pokemon List
```
GET /api/pokemon
```

**Query Parameters:**
- `page` (optional): Page number (default: 1)
- `limit` (optional): Items per page (default: 20)
- `sort` (optional): Sort field (default: "id")
- `type` (optional): Filter by Pokemon type

**Example:**
```bash
curl "http://localhost:8080/api/pokemon?page=1&limit=10&sort=name&type=fire"
```

### 2. Get Captured Pokemon
```
GET /api/captured
```

**Example:**
```bash
curl "http://localhost:8080/api/captured"
```

### 3. Toggle Pokemon Capture
```
POST /api/capture/<pokemon_name>
```

**Example:**
```bash
curl -X POST "http://localhost:8080/api/capture/pikachu"
```

### 4. Get Pokemon Icon URL
```
GET /api/icon/<pokemon_name>
```

**Example:**
```bash
curl "http://localhost:8080/api/icon/pikachu"
```

## Project Structure

```
pokedex/
├── app/
│   ├── __init__.py      # Flask app factory
│   ├── api.py           # API route definitions
│   ├── constants.py     # Application constants
│   ├── services.py      # Business logic
│   ├── state.py         # Application state management
│   └── utils.py         # Utility functions
├── app.py               # Alternative entry point
├── db.py                # Database operations
├── pokemon_db.json      # Pokemon data file
├── requirements.txt     # Python dependencies
├── run.py              # Main entry point
└── README.md           # This file
```

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   - If port 8080 is already in use, you can modify the port in `run.py` or `app.py`
   - Change `app.run(port=8080)` to `app.run(port=8081)` or another available port

2. **Module Not Found Errors**
   - Ensure you're in the correct directory
   - Verify that all dependencies are installed: `pip install -r requirements.txt`
   - Make sure your virtual environment is activated

3. **Database File Missing**
   - Ensure `pokemon_db.json` exists in the project root
   - The application requires this file to function properly

4. **Permission Errors**
   - On macOS/Linux, you might need to use `python3` instead of `python`
   - Ensure you have write permissions in the project directory

### Stopping the Application

To stop the server, press `Ctrl+C` in the terminal where it's running.

## Development

### Adding New Features

1. Add new routes in `app/api.py`
2. Implement business logic in `app/services.py`
3. Update constants in `app/constants.py` if needed
4. Test your changes by restarting the server

### Logging

The application uses Python's logging module. Logs are configured to show INFO level messages and above.

## Data Source

The application uses a local JSON file (`pokemon_db.json`) for Pokemon data and fetches icons from the Pokemon Database website.

## License

This project is for educational/demonstration purposes. 
