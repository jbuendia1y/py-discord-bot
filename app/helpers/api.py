import requests
from os import getenv


class Handle_request:
    __baseUrl: str

    def __init__(self) -> None:
        self.__baseUrl = getenv("API_URL", default="http://localhost:3000")

    def __get_url(self, url: str):
        return self.__baseUrl + url

    def get(self, url: str):
        print(self.__get_url(url))
        response = requests.get(self.__get_url(url))
        return response

    def post(self, url: str, data: dict = None):
        response = requests.post(self.__get_url(url), json=data)
        return response

    def put(self, url: str, data: dict = None):
        return requests.put(self.__get_url(url), json=data)
