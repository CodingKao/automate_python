### Day 9: Basic Web Scraping

# Choose a simple website and write a script to fetch and print its HTML content using the `requests` library.

import requests

def_fetch_html_content(url):
# Send a GET Request to the URL
response = requests.get(url)