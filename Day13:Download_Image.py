### Day 13: Download an Image

# Use the `requests` library to download an image from the webpage to your local machine.

import requests
from bs4 import urljoin
from urllib.parse import urljoin

def fetch_html_content(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')