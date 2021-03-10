import requests
from bs4 import BeautifulSoup


def get_soup(url):

    response = requests.get(url)
    if not response.ok:
        raise Exception(f"not available {url}")

    return BeautifulSoup(response.content, 'html.parser')
