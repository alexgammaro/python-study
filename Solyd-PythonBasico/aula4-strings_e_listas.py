frase = "Oi, tudo bem?"
print(frase)
print(frase[0:7])
print(frase[::-1])
print(frase.lower())
print(frase.upper())
frase_separada = frase.split(",")
print(frase_separada)
frase_nova = frase + " Como vai você?"
print(frase_nova)

lista_nomes = ["João","Maria","Alexandre","Tuca","Luke"]
print(lista_nomes)
print(lista_nomes[0:5:2])
print(lista_nomes[-1])
lista_nomes.append("Geralda")
print(lista_nomes)
lista_nomes.remove("João")
print(lista_nomes)
lista_nomes.insert(2,"Creosvaldo")
print(lista_nomes)
lista_nomes[0] = "Robervania"
print(lista_nomes)
print(lista_nomes.count("Alexandre"))
print(len(lista_nomes))
lista_nomes.clear()
print(lista_nomes)