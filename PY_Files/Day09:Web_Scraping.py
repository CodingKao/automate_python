### Day 9: Basic Web Scraping

# Choose a simple website and write a script to fetch and print its HTML content using the `requests` library.

import requests

def fetch_html_content(url):
    # Send a GET Request to the URL
    response = requests.get(url)

    # Check if the requeest was successful
    if response.status_code == 200:
        # Print the HTML content of the website
        print(response.text)
    else:
        print(f"Failed to fetch the HTML.  Status Code: {response.status_code}")

website_url = 'https://www.python.org/'
fetch_html_content(website_url)