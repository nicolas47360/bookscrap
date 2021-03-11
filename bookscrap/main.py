from bookscrap.categories import get_categories
from bookscrap.books_for_category import get_books_for_category


def get_books_for_categories():
    # Fonction permettant de récupérer toutes les infomations des livres de
    # toutes les catégories.

    url = "https://books.toscrape.com"
    categories = get_categories(url)

    for category_name, category_url in categories.items():
        get_books_for_category(category_url, category_name)
