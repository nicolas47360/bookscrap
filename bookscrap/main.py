import requests
from bs4 import BeautifulSoup
from bookscrap.requester import get_soup
from bookscrap.categories import get_categories
from bookscrap.books_for_category1 import get_books_for_category1


def get_books_for_categories():
    # Fonction permettant de récupérer toutes les infomations des livres de
    # toutes les catégories et l'image de couverture de tous les livres.

    url = "https://books.toscrape.com"
    categories = get_categories(url)

    for category_name, category_url in categories.items():
        all_books = get_books_for_category1(category_url, category_name)
