from configparser import ConfigParser
import google.generativeai as genai

config = ConfigParser()
config.read('credentials.ini')
api_key = config['API_KEY']['google_api_key']

genai.configure(api_key = api_key)

model_gemini_pro = genai.GenerativeModel('gemini-pro')

def identifyKeyFood(description: str) -> str:
    """"
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
    prompt = description + " - What is the main food item (couple of words)"
    response = model_gemini_pro.generate_content(prompt)
    return response.text

