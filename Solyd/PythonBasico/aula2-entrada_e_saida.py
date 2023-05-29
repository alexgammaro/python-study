print("Hello World!")
print("Segundo print")
print("Hello World!\nSegundo print")
print("Hello World!\tSegundo print")

print("==============================================")

nome = input("Escreva seu nome: ")
idade = input("Escreva sua idade: ")
altura = input("Escreva sua altura: ")
salario = 2700.32
tipo_salario = type(salario)
print(nome)
print(type(nome))
print(idade)
print(type(idade))
print(altura)
print(type(altura))
print(salario)
print(tipo_salario)
print(nome, "tem", idade, "anos e tem", str(altura) + "M de altura.")

print("==============================================")

numero1 = 27
numero2 = 53
soma = numero1 + numero2
sub = numero2 - numero1
mult = numero1 * numero2
div = numero2 / numero1
potencia = 10 ** 2 # potência de 10 elevado a 2
raiz_quadrada = 16 ** (1/2) # pega a raíz quadrada
print("A soma é:", soma, "/ A subtracao é:", sub,"/ A multiplicacao é:", mult,"/ A divisao é:", div)
print("10 elevado a 2 é:", potencia)
print("Raiz quadrada de 16 é:", raiz_quadrada)