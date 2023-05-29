a = int(input("Primeiro bimestre: "))
if a > 10:
    a = int(input("Nota digitada incorretamente, por favor corrija. \nPrimeiro bimestre: "))
b = int(input("Segundo bimestre: "))
if b > 10:
    b = int(input("Nota digitada incorretamente, por favor corrija. \nSegundo bimestre: "))
c = int(input("Terceiro bimestre: "))
if c > 10:
    c = int(input("Nota digitada incorretamente, por favor corrija. \nTerceiro bimestre: "))
d = int(input("Quarto bimestre: "))
if d > 10:
    d = int(input("Nota digitada incorretamente, por favor corrija. \nQuarto bimestre: "))
media = (a+b+c+d)/4
print("A média do aluno foi:",media)
# if a<=10 and b<=10 and c<=10 and d<=10:
#     print("A média do aluno foi:",media)
# else:
#     print("Alguma nota foi digitada incorretamente")

# a = int(input("Digite um valor: "))
# if a%2 == 0:
#     print("O número",a,"é par")
# else:
#     print("O número",a,"é impar")
# print("Final do programa")

# a = int(input("Digite o primeiro valor: "))
# b = int(input("Digite o segundo valor: "))
# c = int(input("Digite o terceiro valor: "))
# if a>b and a>c:
#     print("O maior número é o primeiro valor digitado: ",a)
# elif b>a and b>c:
#     print("O maior número é o segundo valor digitado: ",b)
# else:
#     print("O maior número é o terceiro valor digitado: ",c)
# print("Final do programa")