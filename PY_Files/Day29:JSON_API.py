### Day 29: JSON API Interaction

## Extend the script to interact with a JSON-based API, fetch data, and print relevant information.

import requests

def fetch_data():
    # Make a GET request to the API endpoint
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        return data
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

def print_info(data):
    if data:
        # Extract relevant information from the data and print
        print("Data fetched successfully:")
        print("Name:", data.get("name"))
        print("Age:", data.get("age"))
        print("Location:", data.get("location"))
    else:
        print("No data available.")

# Main function to fetch data and print information
def main():
    data = fetch_data()
    print_info(data)

if __name__ == "__main__":
    main()