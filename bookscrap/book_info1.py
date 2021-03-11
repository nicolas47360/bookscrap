from bookscrap.requester import get_soup


def get_book_info(url):
    # Fonction permettant de récupérer les informations d'un livre et retourne
    # un dictionnaire.

    soup = get_soup(url)

    title = soup.find(
        'div', {'class': 'col-sm-6 product_main'}).find('h1').get_text()

    review_rating = soup.find_all(
        'p', {'class': 'star-rating'})[0].get('class')[1]

    category = soup.find('ul', {'class': 'breadcrumb'}
                         ).find_all('a')[2].get_text()

    image_url = soup.find('div', {'class': 'item active'}).find(
        'img')['src'].replace('../..', 'https://books.toscrape.com')

    product_description = soup.find(
        'article', {'class': 'product_page'}).find_all('p')[3].get_text()

    upc = soup.find(
        'table', {'class': 'table table-striped'}).find_all('td')[0].get_text()

    price_excluding_tax = soup.find(
        'table', {'class': 'table table-striped'}).find_all('td')[2].get_text()

    price_including_tax = soup.find(
        'table', {'class': 'table table-striped'}).find_all('td')[3].get_text()

    number_available = soup.find(
        'table', {'class': 'table table-striped'}).find_all('td')[5].get_text()

    return {'product_page_url': url,
            'title': title,
            'review_rating': review_rating,
            'category': category,
            'image_url': image_url,
            'product_description': product_description,
            'upc': upc,
            'price_excluding_tax': price_excluding_tax,
            'price_including_tax': price_including_tax,
            'number_available': number_available}
