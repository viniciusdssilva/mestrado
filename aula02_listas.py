import requests
import json


lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)
# print(lista)

dicionario = {lista[0]:0}

for elemento in lista:
    count = 0
    if elemento in dicionario:
        count = dicionario[elemento] + 1
        dicionario[elemento] = count
    else:
        dicionario[elemento] = 1

print(dicionario)
#    dicionario[elemento] = lista.count[elemento]

# lista.count[13]

#type(lista)
