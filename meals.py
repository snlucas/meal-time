import flask
import meal_functions


app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html', list_meals=meal_functions.list_meals())

@app.route("/id")
def meal_instructions():
    return flask.render_template('meal_instructions')
