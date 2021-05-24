from flask import Flask, render_template, url_for
import meal_functions
import string


application = Flask(__name__)

@application.route("/")
@application.route("/<letter>", methods=["GET"])
def index(letter="a"):
    letter = letter.lower()
    letters = string.ascii_letters
    previous_letter = "" if letter == "a" else letters[letters.index(letter) - 1]
    next_letter = "" if letter == "z" else letters[letters.index(letter) + 1]
    return render_template("index.html", list_meals=meal_functions.list_meals(), letter=letter, previous_letter=previous_letter, next_letter=next_letter)

@application.route("/recipe/<int:id>", methods=["GET"])
def meal_instructions(id):
    meal = meal_functions.get_meal_by_id(id)
    return render_template("meal_instructions.html", meal=meal)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
