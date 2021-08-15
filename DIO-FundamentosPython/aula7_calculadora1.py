class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(10, 2)
print("Valor A é: {}".format(calculadora.valor_a))
print("Valor B é: {}".format(calculadora.valor_b))
print("A + B = {}".format(calculadora.soma()))
print("A - B = {}".format(calculadora.subtracao()))
print("A * B = {}".format(calculadora.multiplicacao()))
print("A / B = {}".format(calculadora.divisao()))

# def soma(a, b):
#     return a + b
#
# def subtracao(s, b):
#     return a - b
#
# def multiplicacao(a, b):
#     return a * b
#
# def divisao(a, b):
#     return a / b
#
# print(soma(1, 2))
# print(soma(3, 4))
# print(subtracao(10, 2))
# print(multiplicacao(10, 2))
# print(divisao(10, 2))