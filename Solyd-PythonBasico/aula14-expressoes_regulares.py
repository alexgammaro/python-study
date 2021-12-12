import re, requests

string_teste = "O gato é bonito"
padrao = re.search(r"\w.+", string_teste) # RAW string

if padrao:
    print(padrao.group())
else:
    print("Padrão não encontrado!")

req = requests.get("http://agsolucoesinfo.000webhostapp.com/contato.htm")
padrao2 = re.findall(r"[\w\.-]+@[\w-]+\.[\w\.-]+", req.text)
# print(req.text)
if padrao2:
    print(padrao2)
else:
    print("Padrão não encontrado!")