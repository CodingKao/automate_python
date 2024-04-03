### Day 29: JSON API Interaction

## Extend the script to interact with a JSON-based API, fetch data, and print relevant information.

import requests

def fetch_data():
    # Make GET request to API
    response = request.get("https://www.python.org/")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        print("Failed to fetch data.  Status code:", response.status_code)
        return None

def print_info(data):
    if data:
        # Extract relevant information from the data and print
        print("Data fetched successfully:")
        print("Name:", data.get("name"))
        print("Age:", data.get("aga"))
        print("Location:", data.get("location"))
    else:
        print("No data available.")
