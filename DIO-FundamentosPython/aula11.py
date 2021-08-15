lista = [1, 10]
try:
    divisao = 10 / 0
    numero = lista[1]
    #x = x
except ZeroDivisionError:
    print("Não é possível realizar divisão por zero (0)")
except IndexError:
    print("Erro ao acessar um índice inválido da lista")
except BaseException as ex:
    print("Erro desconhecido. Erro {}".format(ex))
else:
    print("Executa quando não ocorre exceção")
finally:
    print("Sempre executa")