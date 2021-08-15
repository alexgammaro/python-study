import shutil
def escrever_arquivo(texto):
    arquivo = open("aula9.txt", "w")
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, "a")
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo)
    #print(arquivo.read())
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota_div = aluno_nota.split("\n")
    #print(aluno_nota_div)
    lista_media = []
    for x in aluno_nota_div:
        #print(x)
        aluno_nota_div2 = x.split(",")
        #print(aluno_nota_div2)
        aluno = aluno_nota_div2[0]
        nota1 = int(aluno_nota_div2[1])
        nota2 = int(aluno_nota_div2[2])
        nota3 = int(aluno_nota_div2[3])
        nota4 = int(aluno_nota_div2[4])
        soma_notas = nota1 + nota2 + nota3 + nota4
        media_aluno = soma_notas / 4
        print("O Aluno", aluno, "teve média", media_aluno)
        aluno_nota_div2.pop(0)
        # print(aluno_nota_div2)
        # print(aluno)
        media = lambda notas: sum((int(i) for i in notas)) / 4
        #print(aluno, media(aluno_nota_div2))
        lista_media.append({aluno:media(aluno_nota_div2)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, "../")

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,"../")

if __name__ == '__main__':
    # escrever_arquivo("Primeira linha!\n")
    # aluno = "Alexandre,10,10,10,10"
    # atualizar_arquivo("aula9_notas.txt", aluno)
    # atualizar_arquivo("Terceira linha!\n")
    # ler_arquivo("aula9.txt")
    # lista_media = media_notas("aula9_notas.txt")
    # print(lista_media)
    # copia_arquivo("aula9.txt")
    # move_arquivo("teste.txt")