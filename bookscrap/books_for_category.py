import csv
from bookscrap.requester import get_soup
from bookscrap.links_pages import get_category_pages_urls
from bookscrap.book_links import get_book_links
from bookscrap.book_info import get_book_info
from bookscrap.image import download_image


def get_books_for_category(category_url, category_name):
    # Fonction permettant de récupérer toutes les informations des livres d'une
    # catégorie. Création d'un fichier csv au nom de la catégorie et
    # téléchargement de l'image de couverture associée au livre.

    soup = get_soup(category_url)

    category_pages = get_category_pages_urls(soup, category_url)

    with open('download/' + category_name + '.csv', 'w',
              newline='') as csvfile:
        fieldnames = ['product_page_url', 'title', 'review_rating',
                      'category', 'image_url', 'product_description',
                      'upc', 'price_excluding_tax',
                      'price_including_tax', 'number_available']
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()

        for category_page_url in category_pages:
            for book_url in get_book_links(category_page_url):
                book_info = get_book_info(book_url)
                writer.writerow(book_info)
                image_url = book_info['image_url']
                image_name = book_info['title']
                download_image(image_url, image_name.replace('/', ' '))
