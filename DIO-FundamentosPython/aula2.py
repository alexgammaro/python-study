a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))
print(type(multiplicacao))
print(type(divisao))
print(type(resto))
print("Soma: ",soma)
print("Subtração: " + str(subtracao))
print("Multiplicação: {}".format(multiplicacao))
print("Divisão: " + str(int(divisao)))
print("Resto da divisão: ",resto)
print("===========================")
resultado = ("Soma: {soma} "
      "\nSubtração: {subtracao} "
      "\nMultiplicação: {multiplicacao} "
      "\nDivisão: {divisao} "
      "\nResto da divisão: {resto}".format(soma=soma,
                                           subtracao=subtracao,
                                           multiplicacao=multiplicacao,
                                           divisao=divisao,
                                           resto=resto))
print(resultado)