import requests

def retorna_dados_cep(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/".format(cep))
    print(response.status_code)
    print(type(response.text))
    print(response.text)
    print(type(response.json()))
    print(response.json())
    dados_cep = response.json()
    print(dados_cep["logradouro"])
    print(dados_cep["complemento"])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{}/".format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # #retorna_dados_cep("20261064")
    # dados_pokemon = retorna_dados_pokemon("pikachu")
    # print(dados_pokemon)
    response = retorna_response("http://agsolucoes.info")
    print(response)