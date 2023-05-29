idade = int(input("Entre com sua idade: "))
peso = float(input("Entre com seu peso: "))
altura = float(input("Entre com sua altura: "))

if (idade >= 18 and idade < 60) and (peso >= 60) and (altura >= 1.70):
    print("A pessoa esta apta para entrar no Exercito")
else:
    print("A pessoa não esta apta para entrar no Exercito")