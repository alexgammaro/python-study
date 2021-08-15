import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso")
host = "localhost"
porta = 5432
mensagem = "\nServidor: Olá cliente, blz e você?"
s.bind((host, porta))

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem")
        s.sendto(dados + (mensagem.encode()), end)