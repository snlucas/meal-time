import requests


class RequestHandler():
    def __init__(self, url):
        self.url = url


    # Make a request, and bring meal as a dictionary
    # If is needed a list of meals instead only one, switch 'is_list' arg for True
    # If is needed just one recipe, eg. a search for a meal id, is_list=False will handle it
    def make_request(self, is_list=False):
        r = requests.get(self.url)
        meal = r.json()['meals'][0] if is_list == False else r.json()['meals']
        
        return meal
