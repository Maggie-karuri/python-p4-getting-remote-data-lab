import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url
    
    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    
    def load_json(self):
        response = self.get_response_body()
        return json.loads(response)
    
    def get_user_input(self, prompt):
        user_input = input(prompt)
        return user_input
    
    def get_user_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        url = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        
        response = requests.get(url).json()
        response_formatted = f"Title: {response['docs'][0]['title']}\nAuthor: {response['docs'][0]['author_name'][0]}"
        return response_formatted
