import json

from parser import Pesquisa

# carrega input.json na variavel jason
jason = json.load(open('input.json','r'))
# instancia a classe Pesquisa
p = Pesquisa()
# caso exista a chave "google-me"
if "google-me" in jason:
    lista = jason.get("google-me")
    # faz raspagem de dados
    response = p.parser(lista)
    print(response)
    # transformas dict em str
    stringona = str(response).replace("'", '"')
    # cria output.json
    output = open('output.json', 'w')
    # popula output.json e fecha
    output.write(stringona)
    output.close
