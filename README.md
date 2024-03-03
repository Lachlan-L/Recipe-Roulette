# Code-Technique
A repository for the 2024 UNIHACK Hackathon for the participating team Code Technique

# Inspiration
What on earth do I make for the next meal? How can I save money on my grocery shopping? We have asked ourselves these questions and our solution - Recipe Roulette, answers both these questions.

Say goodbye to meal planning hassles and hello to a delightful fusion of savings and gastronomic creativity with our one-of-a-kind platform! You might be wondering why roulette's in the name -
let's say there's a bit of luck involved in your recipes.

## How to run
Before you can use the Gemini API, you must first obtain an API key. If you don't already have one, create a key with one click in Google AI Studio.
https://aistudio.google.com/app/apikey

Create file named **.env** in route directory and paste in
```
GOOGLE_API_KEY=YOUR_API_KEY
```

Download the dependency:
```
cd backend
pip install -r requirements.txt
```

To run Recipe Roulette:
In two different terminals
```
cd backend
python3 app.py
```
Open localhost:5001 in url
```
cd frontend
npm start
```
Open localhost:3000 in url

# Requirements
Python 3.9 or later

## What it does
Gives a recipe and three ingredients that are needed for the recipe. The ingredients will all be on discount and sale in grocery store websites.

## How we built it
Frontend:
React and CSS: Used to build the user interface and define the aesthetics and layout of the React components.
JavaScript: Controls the behavior of the application, handling user interactions, and passing URL data to the backend.

Backend:
Flask: A Python web framework serving as the intermediary between the frontend and backend which manages incoming requests and responses.
BeautifulSoup: A Python library used to web scrape ingredients on sale and recipes
Gemini: AI that shortens descriptive names of food on discounts to food prompts

## Challenges we ran into
Some grocery store websites blocked scraping so we had to find less prominent websites to supplement the sample space of ingredients.

The names of ingredients we initially got were too long to make into a query for Taste.com which was the website we were getting our recipes from. After trying a variety of options we chose Google Gemini, an AI to parse the ingredient names for us to in order to make it a viable query for Taste.com.

Finding website design ideas to use.

Trying to resolve layout issues such as making the website dynamic and fit to various viewport dimensions. 

## Accomplishments that we're proud of
We got the frontend to connect to the backend even though this was our first time creating a website.
Overall this was just the first time we made a website and we got it functioning.
Learning new languages and software in 1 and a half days.
Understanding the nuances of these softwares to make a functioning website.

## What we learned
We learned how to user Rest API in order to connect the frontend and backend.
How to code an effective frontend display. 
How to effectively work as a team on a local project.

## What's next for Recipe Roulette
Device Despoiler. A website that scrapes affordable electronics from across the internet to find the best deals for electronics and PC parts. So once the user inputs the name of the component or electronic device they want the website will return the cheapest and most reliable option.
