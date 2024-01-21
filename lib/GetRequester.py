import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)

        return response.content

    def load_json(self):
        person_info = []
        info = json.loads(self.get_response_body())
        for i in info:
            person_info.append(i)
        
        return person_info
    
requester = GetRequester(url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
requester.load_json()