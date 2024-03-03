from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get API key from the environment variables
api_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=api_key)

model_gemini_pro = genai.GenerativeModel('gemini-pro')

def identifyKeyFood(description: str) -> str:
    """
    Parameters
    ----------
    description : str
        The descriptive name of the food item

    Returns
    -------
    str
        The food item

    Example
    -------
    Input: Lilydale Free Range Whole Chicken
    Output: Whole Chicken
    """
    prompt = description + " - What is the main food item (in a couple of words)"
    response = model_gemini_pro.generate_content(prompt)
    return response.text

# Usage
#food_description = "RSPCA Approved Chicken Waffles"
# result = identifyKeyFood(food_description)
# print(result)
