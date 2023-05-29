with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.readline()
    print(type(conteudo))
    print(conteudo)
    for linha in arquivo.readlines():
        print(linha)