import random


lista = []

for i in range(0,1000000):
	x = random.randint(1,100000)
	lista.append(x)

dicionario = {}

for elemento in lista:
    if elemento in dicionario:
        dicionario[elemento] += 1
    else:
        dicionario[elemento] = 1

# print(dicionario)
