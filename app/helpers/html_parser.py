from urllib import request
from bs4 import BeautifulSoup


def parser(url: str):
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_content = request.urlopen(req)
    return BeautifulSoup(html_content, "html.parser")
