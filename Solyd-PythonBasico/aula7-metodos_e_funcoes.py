def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
# print(soma(75, 89))
retorno = soma(75, 89)
print(retorno)

def imprime_oi():
    print("Oi")
imprime_oi()

def tem_sete_letras(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False
print(tem_sete_letras("12345678"))
if tem_sete_letras('1234567'):
    print("Realmente tem 7 letras")