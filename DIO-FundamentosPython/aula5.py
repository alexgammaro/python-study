lista = [1, 3, 5 , 7]
lista_animal = ["CAchorro", "Gato", "Elefante"]
print(type(lista))
print(lista)
print(lista_animal[1])

lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

lista.reverse()
lista_animal.reverse()
print(lista)
print(lista_animal)

print(min(lista))
print(max(lista))
print(sum(lista))
print(len(lista_animal))

tupla = (1, 10, 12, 14, "gato", 1)
print(tupla)

tupla_animal = tuple(lista_animal)

novo_animal = input("Digite um animal: ")
if novo_animal in lista_animal:
    print("Existe",novo_animal,"na lista")
else:
    print("Não existe",novo_animal,"na lista")
    print("Adicionando",novo_animal,"na lista")
    lista_animal.append(novo_animal)
for x in lista_animal:
    print(x)

lista_animal.pop()
print(lista_animal)