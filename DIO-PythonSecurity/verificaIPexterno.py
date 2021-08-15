import re, json
from urllib.request import urlopen

url = "https://ipinfo.io/json"

retorno = urlopen(url)

dados = json.load(retorno)

ip = dados["ip"]
hostname = dados["hostname"]
org = dados["org"]
cidade = dados["city"]
pais = dados["country"]
regiao = dados["region"]

print("Detalhes do IP externo\n")
print("IP: {4}\nRegião: {1}\nPaís: {2}\nCidade: {3}\nOrganização: {0}".format(org, regiao, pais, cidade, ip))