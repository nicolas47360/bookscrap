import requests
from bs4 import BeautifulSoup
from bookscrap.requester import get_soup
from bookscrap.count_pages import get_count_pages


def get_category_pages_urls(soup, url):
    # Fonction permettant de récupérer les urls des pages d'une catégorie.

    count = get_count_pages(soup)
    page_url = url[:-10]
    links_url = [url]

    if count == 1:
        return links_url

    for page_number in range(2, count + 1):
        page_number = str(page_number)

        link = (page_url + "page-" + page_number + ".html")
        links_url.append(link)

    return links_url
