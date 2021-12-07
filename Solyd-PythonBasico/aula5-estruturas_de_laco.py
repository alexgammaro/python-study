nomes = ["Alexandre","Karine","Tuca","Luke","Adelaide"]
for nome in nomes:
    print(nome)

for item in range(0, 101, 2):
    print(item)

for i in range(4):
    print(nomes[i])

for i in range(len(nomes)):
    print(nomes[i])
    nomes.append("Layla")
print(nomes)

palavra = "Alexandre Gammaro"
for letra in palavra:
    print(letra)

i = 0
while i < 10:
    print("i (",i ,") ainda é menor que 10")
    i += 1 # Mesma coisa que i = i + 1

lista_frutas = ["maca", "pera", "uva", "abacaxi", "goiaba", "banana"]
contador = 0
for fruta in lista_frutas:
    contador += 1
print(contador)
print(len(lista_frutas))

numero = 0
while True:
    print(numero)
    if numero == 20:
        break
    numero += 1