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

def pesquisar(dicionario,chave):
    busca = dicionario.get(chave)
    if busca != None:
        print("Nome...........: " + busca[0])
        print("Último acesso..: " + busca[1])
        print("Último estação.: " + busca[2])

def excluir(dicionario,chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto eliminado!")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)