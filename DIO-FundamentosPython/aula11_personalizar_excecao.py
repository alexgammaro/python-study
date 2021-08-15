class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input("Entre com um número de 0 a 10: "))
        print(x)
        if x > 10:
            raise InputError("Foi digitado um número maior que 10")
        elif x < 0:
            raise InputError("Foi digitado um número menor que 0")
        break
    except ValueError:
        print("Caracter inválido. Deve-se digitar apenas números!")
    except InputError as ex:
        print(ex)