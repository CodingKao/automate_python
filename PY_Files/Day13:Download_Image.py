### Day 13: Download an Image

# Use the `requests` library to download an image from the webpage to your local machine.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_html_content(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the first image source (src attribute) from the webpage
        image = soup.find('img', src=True)
        if image:
            # Get the absolute URL of the image using urljoin
            image_url = urljoin(url, image['src'])
            
            # Download the image to the local machine
            image_response = requests.get(image_url)
            
            # Check if the image download was successful (status code 200)
            if image_response.status_code == 200:
                # Save the image to a local file
                with open('downloaded_image.jpg', 'wb') as f:
                    f.write(image_response.content)
                
                print("Image downloaded successfully.")
            else:
                print(f"Failed to download the image. Status Code: {image_response.status_code}")
        else:
            print("No image found on the webpage.")
    else:
        print(f"Failed to fetch the HTML. Status Code: {response.status_code}")

website_url = 'https://www.python.org/'
fetch_html_content(website_url)
