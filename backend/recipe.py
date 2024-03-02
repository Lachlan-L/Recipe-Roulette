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
        # Extract the href attribute of each <a> tag
        # for link in recipe_links:
        #     print(link['href'])
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

# getDetails("https://www.taste.com.au/recipes/whole-mandarin-pistachio-cake/c67106ab-3b40-4ca7-9ab5-c44a858cec2b")












# Find all <a> elements with href starting with "/recipes/" and get the text inside them, Remove collections link
# recipe_links_with_text = [(link['href'], link.text) for link in soup.find_all('a', href=lambda href: href and href.startswith('/recipes/') and not href.startswith('/recipes/collections')) if not link.find('img')]
# pageNo += 1
# page = requests.get(url.format(pageNo, ingredients, sort))
# soup = BeautifulSoup(page.content, 'html.parser')
# for link, text in recipe_links_with_text:
#     recipes[text] = link

# print("ok")
# print(recipes["Winter beef salad bowl"])

# Parse HTML
# def scrapePage(soup):
#     # Find all <a> tags with href starting with "/recipes/" but not starting with "/recipes/collections"
#     recipe_links = soup.find_all('a', href=lambda href: href and href.startswith('/recipes/') and not href.startswith('/recipes/collections'))

#     # Initialize variables to store results
#     results = {}

#     # Loop through each <a> tag
#     for link in recipe_links:
#         # Extract the href attribut\me
#         href = link['href']
#         # Check if the <a> tag contains an <img> tag
#         img_tag = link.find('img')
#         if img_tag:
#             # If an <img> tag is found, extract its src attribute
#             results[href] = [img_tag['src']]
#         else:
#             # Extract the text inside the <a> tag
#             results[href].append(link.get_text(strip=True))

#     # Print the extracted data
#     return results

# allResults = {}
# while (not soup.find(string="Oops, something went wrong!")) :
#     result = scrapePage(soup)
#     allResults.update(result)
#     pageNo += 1
#     page = requests.get(url.format(pageNo, ingredients, sort))
#     soup = BeautifulSoup(page.content, 'html.parser')
# print(allResults)