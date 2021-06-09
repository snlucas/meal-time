from app.controller.meal_factory import MealFactory
from flask import Flask, render_template
import string


application = Flask(__name__)
dict_meals  = MealFactory()  # Reusable var


# Route to the first page, and items to the pagination
@application.route("/")
def index():
    letter = "a"
    return render_template("index.html", list_meals=dict_meals.alphabetic_meals, letter=letter, previous_letter="", next_letter="c")


@application.route("/letter/<letter>", methods=["GET"])
def page_letter(letter):
    # Set the pagination
    letter = letter.lower()
    letters = string.ascii_letters  # alphabet letters
    previous_letter = "" if letter == "a" else letters[letters.index(letter) - 1]  # first item of the pagination
    next_letter = "" if letter == "z" else letters[letters.index(letter) + 1]  # last item in the pagination
    return render_template("index.html", list_meals=dict_meals.alphabetic_meals, letter=letter, previous_letter=previous_letter, next_letter=next_letter)


# Show recipe details of an id meal
@application.route("/recipe/<int:id>", methods=["GET"])
def meal_instructions(id):
    meal = dict_meals.search_id_meals_dict(id)
    return render_template("meal_instructions.html", meal=meal)


if __name__ == "__main__":
    application.run(host='0.0.0.0')
