import json

from .parser import Pesquisa

jason = json.load(open('input.json','r'))

if "google-me" in jason:
    lista = jason.get("google-me")
    response = Pesquisa.parser(lista)
    print(response)
    finish = json.dumps(reponse)
