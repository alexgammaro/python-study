import requests

cabecalho = {"User-agent": "Windows 13",
             "Referer": "https://google.com",}

meus_cookies = {"Ultima-visita": "10-10-2030"}

dados = {"username": "zer0f1ll",
         "password": "123456"}

try:
    requisicao = requests.get("http://agsolucoes.info", headers=cabecalho, cookies=meus_cookies, data=dados)
    print(requisicao)
    print(type(requisicao))
    print(requisicao.text)
except Exception as e:
    print("Requisição deu o erro:", e)