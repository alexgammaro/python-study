print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++PROGRAMINHA DE CONTROLE DE FESTINHAS v1.0+++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

numero_convidado = int(input("Quantas pessoas vao a festa? "))
lista_convidado = []

for i in range(1, numero_convidado+1):
    nome_convidado = input("Digite o nome do(a) " + str(i) + "º convidado(a): ")
    lista_convidado.append(nome_convidado)

# print(lista_pessoas)
print("======================================================")
print("====== Lista de pessoas convidadas para a festa ======")
print("======================================================")
for convidado in lista_convidado:
    print(convidado)