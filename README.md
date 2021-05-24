# Meal Time
The purpose of the project is to develop a web app to list TheMealDB meals.
In this project, the main stack is Python and Flask, because it's a simple project, and doesn't need a huge structure.

[Test the App](http://flask-env.eba-k4emjss7.sa-east-1.elasticbeanstalk.com/)

### Status
- [x] Make requests to TheMealDB and made functions to handle the data
- [x] Put the data in the web App
- [x] Use Bootstrap to personalize the App
- [x] Add pagination
- [x] Add Dockerfile
- [x] Make deploy
- [ ] Dark Mode

## Requirements
- **TheMealDB:** Off course it's a fundamental requirement to this app works 😁. You can find more information about TheMealDB API [here](https://www.themealdb.com/api.php).
- **Requests:** Python Requests module made really simple to get data through APIs, and to made requests off course.
- **Flask:** Flask is very useful to create a web project really fast.
- **Bootstrap:** Bootstrap made very easy to write HTML code.

## How to Run
Using **Docker**:
```
$ docker build -t a-tag-name .
$ docker run -p 5000:5000 a-tag-name
```
___
Using **Python**:
```python
$ pip install requirements.txt
$ export FLASK_APP=meals.py
$ export FLASK_ENV=development
$ flask run
```
___
Go to your Web Browser, and search for **127.0.0.1:5000**
