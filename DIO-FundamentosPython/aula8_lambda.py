contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ["cachorro", "gato", "galinha"]
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(5, 10))
print(subtracao(10, 5))

calculadora = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b,
    "divisao": lambda a, b: a / b
}
print(type(calculadora))
soma = calculadora["soma"]
subtracao = calculadora["subtracao"]
multiplicacao = calculadora["multiplicacao"]
divisao = calculadora["divisao"]
print(soma(10, 5))
print(subtracao(10, 5))
print(multiplicacao(10, 5))
print(divisao(10, 5))