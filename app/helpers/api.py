import requests
import os


class Api:
    baseUrl: str

    def __init__(self) -> None:
        self.baseUrl = os.environ["API_URL"]

    def get(self, url: str, json: bool):
        req = requests.get(self.baseUrl + url)
        if json:
            return req.json()
        else:
            return req

    def post(self, url: str, json: bool):
        req = requests.post(self.baseUrl + url)
        if json:
            return req.json()
        else:
            return req
