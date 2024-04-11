### Day 28: Basic HTTP Request

### Use the `requests` library to make a basic HTTP request to a public API and print the response.

print("Script started")

import requests

# Make a GET request to a public API
response = requests.get("https://www.python.org/")

print("Response status code:", response.status_code)

# Check if the GET request was successful
if response.status_code >= 200 and response.status_code < 300:
    print("GET request successful")
    # Print the response
    print(response.text)
else:
    print("Error:", response.status_code)
