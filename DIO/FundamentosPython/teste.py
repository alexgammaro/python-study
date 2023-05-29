import requests
busca = requests.get('https://viacep.com.br/ws/01001000/json/')
status = busca.status_code

def interpretarMensagem(mensagem):
  print('{} {}'.format())

if status == 400:
  print('Mensagem não chegou')
elif status == 200:
  mensagem = busca.json()
  interpretarMensagem(mensagem)
#fim do código.

