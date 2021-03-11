import requests
from bs4 import BeautifulSoup
from bookscrap.requester import get_soup


def download_image(image_url, image_name):
    # Fonction permettant de télécharger l'image de couverture d'un livre.

    response = requests.get(image_url)
    with open('download/' + image_name + '.jpeg', 'wb') as image_file:
        image_file.write(response.content)
