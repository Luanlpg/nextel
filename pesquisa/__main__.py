import json
from parser import Pesquisa

jason = json.load(open('input.json','r'))
p = Pesquisa()

if "google-me" in jason:
    lista = jason.get("google-me")
    response = p.parser(lista)
    print(response)
    stringona = str(response).replace("'", '"')
    output = open('output.json', 'w')
    output.write(stringona)
    output.close
