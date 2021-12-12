import requests, json, time, datetime

while True:
    req = requests.get("https://economia.awesomeapi.com.br/json/USD-BRL")
    # print(req.text)
    cotacao = json.loads(req.text)

    print("===== Cotação de", datetime.datetime.now(), "=====")
    print("Cotação:", cotacao[0]["name"])
    print("Compra:", cotacao[0]["bid"])
    print("Venda:", cotacao[0]["ask"])
    print("Variação:", cotacao[0]["varBid"])
    print("Porcentagem de variação:", cotacao[0]["pctChange"])
    print("Máximo:", cotacao[0]["high"])
    print("Mínimo:", cotacao[0]["low"])
    print("")
    time.sleep(5)