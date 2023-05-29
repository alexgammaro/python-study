lista_de_numeros = [1,2,4,6,7,83,45,2354,674563,22,3,21435345623]

def maior_numero(lista_de_numeros):
    maior = 0
    for numero in lista_de_numeros:
        # print(numero)
        if numero > maior:
            maior = numero
            # print("Esse número é o maior: ",numero)
        # else:
            # print("Não é maior")
    print("O maior número é o", maior)

maior_numero(lista_de_numeros)