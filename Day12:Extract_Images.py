### Day 12: Extract Images
# Extend the script to extract and print all image sources (src attributes) from the webpage.

import requests
from bs4 import BeautifulSoup

def fetch_html_content(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract and print all the links (href attributes) from the webpage
        links = soup.find_all('a', href=True)
        for link in links:
            print(f"Link: {link['href']}")
        
        # Extract and print all image sources (src attributes) from the webpage
        images = soup.find_all('img', src=True)
        for image in images:
            print(f"Image Source: {image['src']}")
    else:
        print(f"Failed to fetch the HTML. Status Code: {response.status_code}")

# Replace 'https://www.python.org/' with the URL of the website you want to scrape
website_url = 'https://www.python.org/'
fetch_html_content(website_url)