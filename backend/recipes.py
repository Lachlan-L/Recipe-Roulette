from bs4 import BeautifulSoup
import requests

# given list of ingredients and sort type
# returns array of links for every recipe
def getRecipes(ingredients, sort):
    url = "https://www.taste.com.au/search-recipes/?page={}&q={}&sort={}"
    pageNo = 1
    page = requests.get(url.format(pageNo, ingredients, sort))
    soup = BeautifulSoup(page.content, 'html.parser')

    recipes = []
    while (not soup.find(string="Oops, something went wrong!")) :
        recipe_links = soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') and tag['href'].startswith('/recipes/') and not tag['href'].startswith('/recipes/collections') and not tag.find('img'))
        recipes = recipes + recipe_links
        pageNo += 1
        page = requests.get(url.format(pageNo, ingredients, sort))
        soup = BeautifulSoup(page.content, 'html.parser')

#rating, relevance, recent, az, cookTime, calories
sort = "az"
ingredients = "mandarin"
getRecipes(ingredients, sort)

# given the exact link to a website recipe taste.com.au
# returns the following dictionary
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
    print(details)