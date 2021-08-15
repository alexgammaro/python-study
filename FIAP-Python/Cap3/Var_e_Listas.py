#Inventário
inventario = []
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Deseja continuar? Digite \"S\": ").upper()
for elemento in (inventario):
    print(elemento)