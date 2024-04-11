### Day 11: Extract Links
# Modify the script to extract and print all the links (href attributes) from the webpage.

import requests
from bs4 import BeautifulSoup

def fetch_html_content(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and print all the links from webpage
        links = soup.find_all('a', href=True)
        for link in links:
            print(f"Link: {link['href']}")

    else:
        print(f"Failed to fetch the HTML.")

website_url = 'http://www.python.org/'
fetch_html_content(website_url)

