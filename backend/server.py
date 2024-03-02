from flask import Flask, request
from recipes import getDetails, getRecipes
import scrape


app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/get-recipe-details", methods=['GET'])
def getRecipeDetails():
    if(request.args.get('url') != None):
        print(getDetails(request.args.get('url')))
        return getDetails(request.args.get('url'))
    else:
        return 'bad request!', 400

@app.route("/get-recipes", methods=['GET'])
def getRecipeList():
    if(request.args.get('ingredients') != None):
        print(getRecipes(request.args.get('ingredients'), "az"))
        return getRecipes(request.args.get('ingredients'), "az")
    else:
        return 'bad request!', 400


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