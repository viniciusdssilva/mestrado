from collections import Counter


def contaCoisas(entrada):
    if type(entrada) == type([]):
        contador = contaLista(entrada)
    elif type(entrada) == type(str()):
        contador = contaTexto(entrada)
    else:
        print("A entrada deve ser uma lista ou um texto.")

    return contador


def contaLista(lista):
    return Counter(lista)


def contaTexto(texto):
    return Counter(texto.split())
