from flask import Flask, render_template, url_for
import meal_functions


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', list_meals=meal_functions.list_meals())

@app.route("/recipe/<int:id>", methods=['GET'])
def meal_instructions(id):
    meal = meal_functions.get_meal_by_id(id)
    return render_template('meal_instructions.html', meal=meal)

if __name__ == "__main__":
   app.run(host='0.0.0.0')
