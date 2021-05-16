import requests
import string


# Make request, and bring recipe as a dictionary
# If is needed a list of recipies instead only one, switch 'is_list' arg for True
def get_meal(meal_url, is_list=False):
    r = requests.get(meal_url)
    meal = r.json()['meals'][0] if is_list == False else r.json()['meals']

    return meal

# Create a recipe with the important data
def recipe(meal):
    name         = meal['strMeal']
    category     = meal['strCategory']
    area         = meal['strArea']
    thumbnail    = meal['strMealThumb']
    instructions = meal['strInstructions']

    return {"name": name, "category": category, "area": area, "thumbnail": thumbnail, "instructions": instructions}

# Search for a meal as string, and return a recipe
def search(meal_name):
    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal_name}"
    meal = get_meal(url)

    return recipe(meal)

# List meals sorting by alphabet
def list_meals():
    page_meals = {}

    for letter in list(string.ascii_lowercase):
        url   = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
        meals = get_meal(url, is_list=True)  # meals list

        # doesn't accept NoneType
        for meal in meals or []:
            recipies = [recipe(meal) for meal in meals]

        page_meals[letter] = recipies  # Add recipies list to the page letter

    return page_meals
