class Calculadora:
    # def __init__(self):
    #     pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
# print("Valor A é: {}".format(calculadora.valor_a))
# print("Valor B é: {}".format(calculadora.valor_b))
print("A + B = {}".format(calculadora.soma(10, 2)))
print("A - B = {}".format(calculadora.subtracao(10, 2)))
print("A * B = {}".format(calculadora.multiplicacao(10, 2)))
print("A / B = {}".format(calculadora.divisao(10, 2)))