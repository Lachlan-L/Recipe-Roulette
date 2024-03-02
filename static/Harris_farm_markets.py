import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def webpage_scraper(url):
    # Fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        product_divs = soup.find_all('div', class_=lambda cls: cls and 'product-item' in cls)

        # Loop through each product div
        for div in product_divs:
            # Find product URL
            product_link = div.find('a', href=True)
            # Find image URL
            image_tag = div.find('img', src=True)
            # Find cost information
            cost_span = div.find('span', class_='unit_price')

            product_path = product_link['href']
            # Extract the image URL
            image_url = image_tag['src']
            product_name = os.path.basename(product_path).replace('-', ' ').title()
            cost = cost_span.text.strip() if cost_span else 'Price not available'

            # Print the product details
            product_dict = {
                    'name': product_name,
                    'cost': cost,
                    'image': image_url
                }
            print(product_dict)

    else:
        print('Failed to fetch webpage:', response.status_code)

webpage_scraper('https://www.harrisfarm.com.au/collections/online-specials')