from flask import Flask, request
from recipes import getRandomRecipeJson
import scrape


app = Flask(__name__)

@app.route('/')

@app.route("/members")
def members():
    return {"title": "apple-pie", "image": "apple_png.png", "ingredients": ["apple", "lettuce"]}


# Example return value
# {
#     "url": "https://www.taste.com.au/recipes/warm-citrus-fruit-cardamom-cream/0088ecee-aee2-4a91-94da-039562f9d8a0",
#     "title": "Warm citrus fruit in cardamom cream",
#     "image": "/assets/static/images/generic-placeholder.jpg",
#     "ingredients": [
#         "20g (1 tbsp) butter or margarine",
#         "2 tbsp brown sugar",
#         "1/2 tsp ground cardamom",
#         "80mls (1/3 cup) thickened cream",
#         "3 tangelos, peeled, segmented",
#         "2 mandarins, peeled, segmented"
#     ]
# }
@app.route("/get-recipe-details", methods=['GET'])
def getRecipeDetails():
    if(request.args.get('ingredients') != None):
        obj = getRandomRecipeJson(request.args.get('ingredients'), "az")
        print(obj)
        return obj
    else:
        return 'bad request!', 400

# @app.route("/get-recipes", methods=['GET'])
# def getRecipeList():
#     if(request.args.get('ingredients') != None):
#         print(getRecipes(request.args.get('ingredients'), "az"))
#         return getRecipes(request.args.get('ingredients'), "az")
#     else:
#         return 'bad request!', 400


@app.route("/get-ingredient", methods=['GET'])
def getIngredient():
    if(request.args.get('category') != None):
        if (request.args.get('category') == 'Meat'):
            return scrape.randomSelect(scrape.readData('backend/data/meat.json'))
        elif (request.args.get('category') == 'Vegetable'):
            return scrape.randomSelect(scrape.readData('backend/data/vegetable.json'))
        elif (request.args.get('category') == 'Fruit'):
            return scrape.randomSelect(scrape.readData('backend/data/fruit.json'))
        elif (request.args.get('category') == 'Seafood'):
            return scrape.randomSelect(scrape.readData('backend/data/seafood.json'))
    else:
        return 'bad request!', 400


if __name__ == "__main__":
    scrape.outputData(scrape.meatScrape(), 'backend/data/meat.json')
    scrape.outputData(scrape.vegetableScrape(), 'backend/data/vegetable.json')
    scrape.outputData(scrape.seafoodScrape(), 'backend/data/seafood.json')
    scrape.outputData(scrape.fruitScrape(), 'backend/data/fruit.json')
    app.run(debug = True, port = 5001)
    print("hello world!")