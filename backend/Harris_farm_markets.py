import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re

def webpage_scraper(url):
    # Fetch the webpage content
    response = requests.get(url)
    returnObj = []

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        product_divs = soup.find_all('div', class_=lambda cls: cls and 'product-item' in cls)
        print(soup.find(class_="is-special"))

        # Loop through each product div
        for div in product_divs:
            # Find product URL
            product_link = div.find('a', href=True)
            # Find image URL
            image_tag = div.find('img', src=True)
            # Find cost information
            cost_span = div.find('span', class_='from_price')
            if cost_span is None:
                print("FAIL")
                continue
            else:
                product_path = product_link['href']
                # Extract the image URL
                image_url = image_tag['src']
                product_name = os.path.basename(product_path).replace('-', ' ').title()
                cost = cost_span.text.strip() if cost_span else 'Price not available'

                pattern = re.compile(r'\d+$')
                # Check if the string ends with a number
                match = pattern.search(product_name)
                # If a number is found at the end, remove it
                if match:
                    product_name = product_name[:match.start()]

                product_name = product_name.rstrip()
                # Print the product details
                product_dict = {
                        'name': product_name,
                        'cost': cost,
                        'image': image_url
                    }

                returnObj.append(product_dict)
        return returnObj
    else:
        print('Failed to fetch webpage:', response.status_code)

def harrisVegScrape():
    return webpage_scraper("https://www.harrisfarm.com.au/collections/vegies-specials")

def harrisFruitScrape():
    return webpage_scraper("https://www.harrisfarm.com.au/collections/fruit-specials")

def harrisMeatScrape():
    return webpage_scraper("https://www.harrisfarm.com.au/collections/butcher-specials")

def harrisSeafoodScrape():
    return webpage_scraper("https://www.harrisfarm.com.au/collections/seafood-specials")



# print(webpage_scraper('https://www.harrisfarm.com.au/collections/online-specials'))
for obj in harrisVegScrape():
    print(obj)