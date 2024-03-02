from flask import Flask, request
from recipes import getDetails, getRecipes


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

if __name__ == "__main__":
    app.run(debug = True)