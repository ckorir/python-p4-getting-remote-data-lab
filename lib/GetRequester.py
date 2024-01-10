import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

        pass

    def load_json(self):
        response_body = self.get_response_body()
        json_content = json.loads(response_body)  # Use json.loads to parse the JSON content
        return json_content
        pass