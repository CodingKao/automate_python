### Day 10: Parsing HTML
# Integrate `BeautifulSoup` to parse the HTML fetched on Day 9 and print the title of the webpage.

import requests
from bs4 import BeautifulSoup

def fetch_html_content(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and print the title of the webpage
        title = soup.title.text
        print(f"Title of the webpage: {title}")
    else:
        print(f"Failed to fetch the HTML.  Status COde: {response.status_code}")


website_url = 'http://www.python.org/'
fetch_html_content(website_url)

