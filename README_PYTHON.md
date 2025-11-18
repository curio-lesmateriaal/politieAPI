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
- 🔐 API key authentication

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## API Key Setup (Laravel)

1. Add the API key to your Laravel `.env` file:

```env
API_KEY=your-secret-api-key-here
```

2. Make sure your Laravel API server is running

## Usage

1. Make sure your Laravel API server is running (default: `http://politieapi.test`)
2. Run the Python script:

```bash
python police_lookup.py
```

Or on Unix/Linux/Mac:

```bash
chmod +x police_lookup.py
./police_lookup.py
```

3. **First time setup**: Use menu option 8 to set your API key

## Configuration

The default API URL is set to `http://politieapi.test/api`. You can change it:
- Edit the `API_BASE_URL` variable in `police_lookup.py`
- Or use option 7 in the menu to change it at runtime

**API Key Configuration:**
- Set the `API_KEY` variable in `police_lookup.py` (not recommended for security)
- Or use menu option 8 to set it at runtime (recommended)

## Menu Options

1. **List all investigations** - Shows all available investigations (titles only)
2. **Get investigation by ID** - View detailed information about a specific investigation (title only)
3. **List all witnesses** - Shows all registered witnesses
4. **Get witness by ID** - View detailed information about a specific witness
5. **List all people** - Shows all people in the database
6. **Get person by ID** - View detailed information about a specific person
7. **Change API URL** - Update the API base URL
8. **Set API Key** - Configure your API key for authentication
0. **Exit** - Quit the application

## API Endpoints Used

- `GET /api/investigations` - Get all investigations
- `GET /api/investigations/{id}` - Get investigation by ID
- `GET /api/witnesses` - Get all witnesses
- `GET /api/witnesses/{id}` - Get witness by ID
- `GET /api/people` - Get all people
- `GET /api/people/{id}` - Get person by ID

## Authentication

All API endpoints require authentication via API key. The API key must be:
- Set in your Laravel `.env` file as `API_KEY`
- Sent in the `X-API-Key` header with each request
- Configured in the Python app using menu option 8

If you don't have an API key configured, you'll see an error message prompting you to set one.

## Notes

- The application uses colored output for better readability
- All API errors are handled gracefully with helpful error messages
- The console clears on startup for a clean experience
- API key is masked in the display for security (shows first 4 and last 4 characters)


