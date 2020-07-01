def sommaLista(lista):
    somma=0
    for i in lista:
        somma+=sum(i)
    return somma





if __name__ == '__main__':
    lista= [[1,2,3], [3]]
    somma=sommaLista(lista)
    print(somma)