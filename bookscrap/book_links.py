from bookscrap.requester import get_soup


def get_book_links(category_page_url):
    # Fonction permettant de récupérer les urls des livres d'une page.

    soup = get_soup(category_page_url)
    links = []

    books = soup.select('ol.row div.image_container a')
    for a in books:
        link = a['href'].replace('../../..', 'catalogue')
        links.append("https://books.toscrape.com/" + link)

    return links
