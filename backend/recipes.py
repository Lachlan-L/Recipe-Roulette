from bs4 import BeautifulSoup, SoupStrainer
import requests
import json

# given list of ingredients and sort type
# returns array of links for every recipe
def getRecipes(ingredients, sort):
    url = "https://www.taste.com.au/search-recipes/?page={}&q={}&sort={}"
    pageNo = 1
    page = requests.get(url.format(pageNo, ingredients, sort))
    only_a_tags = SoupStrainer("a")
    soup = BeautifulSoup(page.content, 'html.parser', parse_only=only_a_tags)

    links = []
    while (not soup.find(string="Oops, something went wrong!")) :
        recipeLinks = soup.find_all(lambda tag: tag.get('href') and tag['href'].startswith('/recipes/') and not tag['href'].startswith('/recipes/collections') and not tag.find('img'))
        # Extract the href attribute of each <a> tag and append to all_links list
        for link in recipeLinks:
            links.append(link['href'])
        pageNo += 1
        page = requests.get(url.format(pageNo, ingredients, sort))
        soup = BeautifulSoup(page.content, 'html.parser')
    json_string = json.dumps(links)
    return json_string

#rating, relevance, recent, az, cookTime, calories
sort = "az"
ingredients = "mandarin"
# print(getRecipes(ingredients, sort))

# given the exact link to a website recipe taste.com.au
# returns the following json
# {
#  title: apple pie
#  image: apple_pie.png
#  ingredients: [apple, pie]
# }
def getDetails(recipeUrl):
    page = requests.get(recipeUrl)
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.find(class_ = "main-icon")['src']
    title = soup.find('div', class_='recipe-title-container').find('h1').text.strip()
    ingredients = [div.text.strip() for div in soup.find_all('div', class_="ingredient-description")]
    details = {"title": title, "image": img, "ingredients": ingredients}
    json_string = json.dumps(details, indent=4)
    return json_string
