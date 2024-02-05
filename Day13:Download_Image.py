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

        # Extract the first image source (src attribute) from the webpate
        image = soup.find('img', src=True)
        if image:
            # Get the absolute URL of the image using urljoin
            image_url = urljoin(url, image['src'])

            # Download the image to the local machine
            image_response = requests.get(image_url)

            # Check if the image download succeeded
            if image_response.status_code == 200:
                # Save the image to a local file
                with open('download_image.jpd', 'wb') as f:
                    f.write(image_response.content)