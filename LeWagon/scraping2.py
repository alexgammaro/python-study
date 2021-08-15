import requests
from bs4 import BeautifulSoup

page = 1
for page in range(1, 51):
    link = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
    response = requests.get(link)
    html = response.content
    scraped = BeautifulSoup(html, 'html.parser')
    # print(link)
    items = scraped.find_all('article', class_='product_pod')
    title_prices = []
    for item in items:
        title = item.h3.a['title']
        link = item.h3.a['href']
        price = item.find('p', class_='price_color')
        price_float = float(price.text.lstrip('£'))
        title_prices.append(
            {title: price_float}
        )
    print(title_prices)