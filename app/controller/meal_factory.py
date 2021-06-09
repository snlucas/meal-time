import string
from .request_handler import RequestHandler
from ..model.meal import Meal


class MealFactory():
    def __init__(self):
        self.alphabetic_meals = self.make_alphabetic_meals_dict()  # Reusable meals dict


    # Dict with meals list, alphabetic sorting
    # {a: '...', b: '...', ...}
    def make_alphabetic_meals_dict(self):
        page_meals = {}  # dict with alphabetic letters
        list_meals = []  # list with meals

        # For each alphabet letter
        # Create a Meal object, and add to the meals dict
        for letter in list(string.ascii_lowercase):
            url   = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
            meals = RequestHandler(url).make_request(is_list=True)  # meals list

            # doesn't accept NoneType (So if so, return [])
            # Get data to create a Meal object, and append to a list
            for meal in meals or []:
                meal_id           = meal['idMeal']
                meal_name         = meal['strMeal']
                meal_category     = meal['strCategory']
                meal_area         = meal['strArea']
                meal_thumbnail    = meal['strMealThumb']
                meal_instructions = meal['strInstructions']
                
                list_meals.append(Meal(meal_id, meal_name, meal_category, meal_area, meal_thumbnail, meal_instructions))
                
            page_meals[letter] = list_meals[:]  # Set a clone of meals list to the page letter
            list_meals.clear()  # Reset list

        return page_meals


    # Return a Meal Object searching for it's id
    def search_id_meals_dict(self, id):
        for letter in self.alphabetic_meals.values():
            # Not count null values
            if len(letter) > 0:
                for meal in letter:
                    if int(meal.id) == id:
                        return meal
