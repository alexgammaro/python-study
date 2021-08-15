# a = int(input("Digite um valor: "))
# div = 0
# for x in range(1,a+1):
#     resto = a%x
#     print("O número",a,"ao dividir por",x,"tem como resto",resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print("Logo, o número {} é primo".format(a))
# else:
#     print("Logo o número {} não é primo".format(a))

# for num in range(101):
#     div = 0
#     for x in range(1,num+1):
#         resto = num%x
#         #print("O número",num,"ao dividir por",x,"tem como resto",resto)
#         if resto == 0:
#            div += 1
#     if div == 2:
#         print("O número {} é primo".format(num))
#     # else:
#     #     print("O número {} não é primo".format(num))

nota1 = int(input("Digite a nota do primeiro bimestre: "))
while nota1 > 10:
    print("Você digitou a nota errada, Lembre-se: A nota deve ser de 0 a 10")
    nota1 = int(input("Entre novamente com a nota do primeiro bimestre: "))
nota2 = int(input("Digite a nota do segundo bimestre: "))
while nota2 > 10:
    print("Você digitou a nota errada, Lembre-se: A nota deve ser de 0 a 10")
    nota2 = int(input("Entre novamente com a nota do segundo bimestre: "))
nota3 = int(input("Digite a note do terceiro bimestre: "))
while nota3 > 10:
    print("Você digitou a nota errada, Lembre-se: A nota deve ser de 0 a 10")
    nota3 = int(input("Entre novamente com a nota do terceiro bimestre: "))
nota4 = int(input("Quarto bimestre: "))
while nota4 > 10:
    print("Você digitou a nota errada, Lembre-se: A nota deve ser de 0 a 10")
    nota4 = int(input("Entre novamente com a nota do quarto bimestre: "))
media = (nota1+nota2+nota3+nota4)/4
print("A média do aluno foi:",media)