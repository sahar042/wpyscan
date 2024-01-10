import requests

class UserPosts:
    def __init__(self, username, found_by, confidence):
        self.username = username
        self.found_by = found_by
        self.confidence = confidence

class TargetPosts:
    def __init__(self, homepage_url):
        self.homepage_url = homepage_url

    def get_response(self, url):
        response = requests.get(url)
        return response