# import time

# def abre_arquivo():
#     try:
#         arquivo = open("arquivo2.txt")
#         return arquivo
#     except Exception as erro:
#         print("Aconteceu o erro", erro)
#         return False
#
# while not abre_arquivo():
#     print("Tentando abrir o arquivo")
#     abre_arquivo()

try:
    a = 1200 / 0
except ZeroDivisionError:
    print("Não é possível realizar divisão por 0")

print("Continuação do código")

try:
    adasdad()
except Exception as erro:
    print("Aconteceu o erro", erro)