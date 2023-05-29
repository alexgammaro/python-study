import socket

resp = "S"
while(resp == "S"):
    url = input("Digite uma URL: ")
    ip = socket.gethostbyname(url)
    print("O endereço de IP referente à URL informada é: ", ip)
    resp = input("Digite <S> para continuar: ").upper()