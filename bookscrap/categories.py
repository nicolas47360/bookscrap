from bookscrap.requester import get_soup


def get_categories(url):
    # Fonction permettant des récupérer les urls des catégories ainsi que le
    # nom des catégories dans un dictionnaire.

    soup = get_soup(url)

    categories = soup.find(
        "ul", {'class': 'nav nav-list'}).find('ul').find_all('li')
    categories_urls = {}

    for li in categories:
        links = li.find('a')['href']
        category_name = li.find('a').get_text().replace(
            '\n', '').replace(' ', '').strip().lower()
        categories_urls[category_name] = "https://books.toscrape.com/" + links

    return categories_urls
