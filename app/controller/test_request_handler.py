import unittest
import requests


class TestRequestHandler(unittest.TestCase):
    def test_request_get_successful_status_code(self):
        # Test if a request using letter key is within the successful status code range
        letter  = "a"
        url     = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
        request = requests.get(url)
        self.assert_(200 <= request.status_code < 300, "Bad status")
    

    def test_request_get_non_empty_list(self):
        # Test if request using letter key, and parent key get a non empty list
        parent_key = "meals"
        letter     = "a"
        url        = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
        request    = requests.get(url)
        self.assertGreaterEqual(len(request.json()[parent_key]), 1, "Empty response list")


    def test_request_get_right_keys(self):
        # Test if request using letter key get right keys used in the project
        used_keys = {"idMeal", "strMeal", "strCategory", "strArea", "strMealThumb", "strInstructions"}
        letter    = "a"
        url       = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
        request   = requests.get(url)
        response  = request.json()["meals"]
        self.assert_(used_keys.issubset(response[0].keys()), "Some key isn't right")


if __name__ == "__main__":
    unittest.main()
