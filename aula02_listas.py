import requests
import json


lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)
# print(lista)

dicionario = {}

for elemento in lista:
    if elemento in dicionario:
        dicionario[elemento] += 1
    else:
        dicionario[elemento] = 1

print(dicionario)

#    dicionario[elemento] = lista.count[elemento]

# lista.count[13]

#type(lista)
