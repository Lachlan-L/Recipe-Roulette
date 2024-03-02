from flask import Flask, request
from recipes import getRandomRecipeJson
import scrape


app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


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
        print(getRandomRecipeJson(request.args.get('ingredients'), "az"))
        return getRandomRecipeJson(request.args.get('ingredients'), "az")
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
        if (request.args.get('category') == 'meat'):
            return scrape.randomSelect(scrape.meatScrape())
        elif (request.args.get('category') == 'vegetable'):
            return scrape.randomSelect(scrape.vegetableScrape())
        elif (request.args.get('category') == 'fruit'):
            return scrape.randomSelect(scrape.fruitScrape())
        elif (request.args.get('category') == 'seafood'):
            return scrape.randomSelect(scrape.seafoodScrape())
    else:
        return 'bad request!', 400


if __name__ == "__main__":
    app.run(debug = True)