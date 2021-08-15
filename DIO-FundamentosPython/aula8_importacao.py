from aula8_televisao import Televisao
from aula8_calculadora2 import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora()
    print(calculadora.soma(5, 10))

    lista = ["cachorro", "gato", "galinha"]
    print(contador_letras(lista))
    print(teste())