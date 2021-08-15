def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> - Para Inserir um usuário\n" +
                 "<P> - Para Pesquisar um usuário\n" +
                 "<E> - Para Excluir um usuário\n" +
                 "<L> - Para Listar os usuários: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))

def pesquisar(dicionario,chave):
    with open("bd.txt", "r") as arquivo:
        busca = arquivo.read()
        if busca != None:
            print(busca)
    # if busca != None:
    #     print("Nome...........: " + busca[0])
    #     print("Último acesso..: " + busca[1])
    #     print("Último estação.: " + busca[2])

def excluir(dicionario,chave):
    # with open("bd.txt", "a") as arquivo:
    #     for chave, valor in dicionario
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto eliminado!")

def listar(dicionario):
    with open("bd.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            print(linha)