import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
html = response.content
scraped = BeautifulSoup(html, 'html.parser')
print(scraped.title.text.strip())
print(scraped.find('title').text.strip())

full_title = scraped.find('article', class_='product_pod').h3.a['title']
# print(full_title)

items = scraped.find_all('article', class_='product_pod')
# print(type(items))
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

# for price in prices:
#     price = float(price.text.lstrip('£'))
#     print(price)

div = scraped.select('div') # elements
classes = scraped.select('.product_pod') # class
id = scraped.select('#messaes') # id
h1 = scraped.select('h1')
h3 = scraped.select('h3')
print(h3)