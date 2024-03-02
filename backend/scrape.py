import Harris_farm_markets
import requests
from bs4 import BeautifulSoup
import random
import urllib.parse
import json

# QUICK INTRO: MOST IMPORTANT FUNCTIONS

# SELF EXPLANATORY: returns array of ingredient objects
# meatScrape
# vegetableScrape
# seafoodScrape
# fruitScrape

# returns JSON of (1 ingredient object given an input array)
# randomSelect


def colesScrape(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    returnArray = []
    pageNum = 1
    while (len(soup.findAll(attrs={'class': 'sc-6fb8ea3a-3 kzXkbX coles-targeting-ProductTileProductTileWrapper'})) != 0):
        objs = soup.findAll(attrs={'class': 'sc-6fb8ea3a-3 kzXkbX coles-targeting-ProductTileProductTileWrapper'})
        for obj in objs:
            soup = BeautifulSoup(str(obj), "html.parser")
            NAMETAG = soup.find(class_="product__title")
            COSTTAG = soup.find(class_="price__value")
            SAVEDTAG = soup.find(class_="badge-label")
            LINKTAG = soup.find('img', src=True)

            # Split the partial URL to extract the query string
            query_string = LINKTAG['src'].split('?')[1]

            # Parse the query string and extract the 'url' parameter
            parsed_query = urllib.parse.parse_qs(query_string)
            url_parameter = parsed_query['url'][0]

            # Decode the URL encoding
            imageLink = urllib.parse.unquote(url_parameter)


            name = NAMETAG.text.split('|')[0]
            name = name.replace("Coles ", "")

            if SAVEDTAG:
                saved = SAVEDTAG.text

            newObj = {}
            newObj['name'] = name
            newObj['cost'] = float(COSTTAG.text[1:])
            newObj['image'] = imageLink
            # newObj['saved'] = float(saved.split(" ")[1][1:])

            returnArray.append(newObj)

        pageNum = pageNum + 1
        URL = URL[:-1] + str(pageNum)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
    return returnArray

def aldiScrape(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    objs = soup.find_all(class_="box--wrapper ym-gl ym-g25")

    returnArray = []
    for obj in objs:
        soup = BeautifulSoup(str(obj), "html.parser")
        NAMETAG = soup.find(class_="box--description--header")
        COSTTAG = soup.find(class_="box--value")
        CENTTAG = soup.find(class_="box--decimal")

        imageLink = obj.find('img')['src']
        newObj = {}
        newObj['name'] = NAMETAG.text.strip()
        newObj['cost'] = float(COSTTAG.text[1:] + CENTTAG.text)
        newObj['image'] = imageLink

        returnArray.append(newObj)
    return returnArray

def meatScrape():
    returnObj = colesScrape("https://www.coles.com.au/on-special/meat-seafood/bbq-sausages-burgers?page=1")
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/beef-veal?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/game?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/hams-bacon?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/lamb?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/mince?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/organic-meat?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/pork?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/poultry?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/meat-free-range?page=1"):
        returnObj.append(obj)
    for obj in Harris_farm_markets.harrisMeatScrape():
        returnObj.append(obj)
    return returnObj

def vegetableScrape():
    array = colesScrape("https://www.coles.com.au/on-special/fruit-vegetables/vegetables?page=1")
    for obj in Harris_farm_markets.harrisVegScrape():
        array.append(obj)
    return array

def fruitScrape():
    array = colesScrape("https://www.coles.com.au/on-special/fruit-vegetables/fruit?page=1")
    for obj in Harris_farm_markets.harrisFruitScrape():
        array.append(obj)
    return array

def seafoodScrape():
    array =  colesScrape("https://www.coles.com.au/on-special/meat-seafood/seafood?page=1")
    for obj in Harris_farm_markets.harrisSeafoodScrape():
        array.append(obj)
    return array

def randomSelect(array):
    return json.dumps(random.choice(array))

# FRUIT "https://www.coles.com.au/on-special/fruit-vegetables/fruit?page=1"
# VEGETABLE "https://www.coles.com.au/on-special/fruit-vegetables/vegetables"
# SEAFOOD "https://www.coles.com.au/on-special/meat-seafood/seafood"

# MEAT
# https://www.coles.com.au/on-special/meat-seafood/bbq-sausages-burgers
# https://www.coles.com.au/on-special/meat-seafood/beef-veal
# https://www.coles.com.au/on-special/meat-seafood/game
# https://www.coles.com.au/on-special/meat-seafood/hams-bacon
# https://www.coles.com.au/on-special/meat-seafood/lamb
# https://www.coles.com.au/on-special/meat-seafood/mince
# https://www.coles.com.au/on-special/meat-seafood/organic-meat
# https://www.coles.com.au/on-special/meat-seafood/pork
# https://www.coles.com.au/on-special/meat-seafood/poultry


# VEGAN MEAT https://www.coles.com.au/on-special/meat-seafood/meat-free-range

# TEST = "https://www.coles.com.au/on-special/meat-seafood?page=1"
# print(colesScrape(TEST))
# TEST = "https://www.iga.com.au/low-prices-every-day/"
# wooliesScrape(TEST)

# TEST = "https://www.aldi.com.au/groceries/super-savers/"
# print(aldiScrape(TEST))

# for obj in meatScrape():
#     print(obj)
# meatScrape()
# vegetableScrape()
# fruitScrape()
# FINAL = randomSelect(seafoodScrape())
# print(FINAL)