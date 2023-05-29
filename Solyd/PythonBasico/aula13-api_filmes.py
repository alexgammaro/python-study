'''
Here is your key: bc8268fe

Please append it to all of your API requests,

OMDb API: http://www.omdbapi.com/?i=tt3896198&apikey=bc8268fe

Click the following URL to activate your key: http://www.omdbapi.com/apikey.aspx?VERIFYKEY=812d62b5-55f6-488b-89ee-21566639c141
If you did not make this request, please disregard this email.
'''

import requests, json

def requisicao(filme):
    try:
        req = requests.get("http://www.omdbapi.com/?apikey=bc8268fe&t=" + filme)
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print("Erro na conexão!")
        return None

def printar_detalhes(filme):
    print("Título:", filme["Title"])
    print("Atores:", filme["Actors"])
    print("Diretor:", filme["Director"])
    print("Ano:", filme["Year"])
    print("Prêmios:", filme["Awards"])
    print("Poster:", filme["Poster"])
    print("Nota IMDB:", filme["imdbRating"])
    print("")

sair = False
while not sair:
    op = input("Escreva o nome de um filme ou SAIR para fechar: ")
    if op == "SAIR" or "sair":
        sair = True
        print("Saindo...")
    else:
        filme = requisicao(op)
        if filme["Response"] == "False":
            print("Filme não encontrado")
        else:
            printar_detalhes(filme)