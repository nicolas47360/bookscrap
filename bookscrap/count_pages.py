
import requests
from bs4 import BeautifulSoup
from bookscrap.requester import get_soup


def get_count_pages(soup):
    # Fonction permettant de donner le nombre de page d'une catégorie.

    ul_element = soup.find("ul", {"class": "pager"})
    if ul_element:
        li_element = ul_element.find("li", {"class": "current"})
        if li_element:
            return int(li_element.get_text().replace(' Page 1 of ', ''))

    return 1
