import requests
import json

class GetRequester:

    def __init__(self, url=" https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"): #initialize a string with a URL
        self.url = url

    def get_response_body(self): #sends a GET request to a URL passed in thi init that returns the body pf ther espont  
        response = requests.get(self.url)
        return response.content

    def load_json(self): #use get_response_body to send a request, then return a Python list or dictionary made up of data converted from the response of that request.
        response = requests.get(self.url)
        return response.json()