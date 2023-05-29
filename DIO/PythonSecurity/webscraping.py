from bs4 import BeautifulSoup
import requests

host = input("Digite o site a fazer o Web Scraping: ")
site = requests.get(host).content
#objeto site está recebendo o conteúdo da requisição http no site.
soup = BeautifulSoup(site, "html.parser")
#objeto soup está baixando do site o html.
# print(soup.prettify())
#transforma o html em string e o print irá exibir o html.

# temperatura = soup.find("span", class_="_block _margin-b-5 -gray")
# print(temperatura.string)
print(soup.title.string)
print(soup.a.string)
print(soup.p.string)
print(soup.find("admin"))