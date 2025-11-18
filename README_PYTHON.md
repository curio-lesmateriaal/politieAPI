# Politie API Python Console Lookup Tool

A cool command-line interface for querying the Politie API with police-themed ASCII art!

## Features

- 🚔 Cool police ASCII art header
- 📋 Browse all investigations
- 🔍 Look up specific investigations by ID
- 👥 View all witnesses
- 👤 View all people
- 🎨 Colorful terminal output
- ⚙️ Configurable API URL

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Make sure your Laravel API server is running (default: `http://localhost:8000`)
2. Run the Python script:

```bash
python police_lookup.py
```

Or on Unix/Linux/Mac:

```bash
chmod +x police_lookup.py
./police_lookup.py
```

## Configuration

The default API URL is set to `http://localhost:8000/api`. You can change it:
- Edit the `API_BASE_URL` variable in `police_lookup.py`
- Or use option 7 in the menu to change it at runtime

## Menu Options

1. **List all investigations** - Shows all available investigations
2. **Get investigation by ID** - View detailed information about a specific investigation
3. **List all witnesses** - Shows all registered witnesses
4. **Get witness by ID** - View detailed information about a specific witness
5. **List all people** - Shows all people in the database
6. **Get person by ID** - View detailed information about a specific person
7. **Change API URL** - Update the API base URL
0. **Exit** - Quit the application

## API Endpoints Used

- `GET /api/investigations` - Get all investigations
- `GET /api/investigations/{id}` - Get investigation by ID
- `GET /api/witnesses` - Get all witnesses
- `GET /api/witnesses/{id}` - Get witness by ID
- `GET /api/people` - Get all people
- `GET /api/people/{id}` - Get person by ID

## Notes

- The application uses colored output for better readability
- All API errors are handled gracefully with helpful error messages
- The console clears on startup for a clean experience


