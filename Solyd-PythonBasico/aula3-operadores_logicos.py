# Comparadores: ==  !=  >  <  >=  <=  and  or  not
var_verdade = True # Boolean
var_falso = False # Boolean
print(type(var_verdade), type(var_falso))
print(var_verdade, var_falso)
if var_verdade == True:
    print("var_verdade é:", var_verdade)

a = 50
b = 30
if a > b:
    print(a, "é maior do que", b)
else:
    print(a,"não é maior do que", b)

print("Opcoes\n1 = escreve Alexandre\n2 = escreve Joao\n3 = escreve Maria")
opcao = input("Escolha um opcao: ")
if opcao == '1':
    print("Alexandre")
elif opcao == '2':
    print("Joao")
elif opcao == '3':
    print("Maria")
else:
    print("Opcao invalida")

print(True)
print(not True)

if True:
    print("Entrou no if")
else:
    print("Entrou no else")

if not True:
    print("Entrou no if")
else:
    print("Entrou no else")