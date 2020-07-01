def sommaCumulata(lista):
    listaSomme=[]
    somma=0
    for i in lista:
        somma+=i
        listaSomme.append(somma)
    return listaSomme





if __name__ == '__main__':
    lista= [1,2,3,4,5]
    somma=sommaCumulata(lista)
    print(somma)