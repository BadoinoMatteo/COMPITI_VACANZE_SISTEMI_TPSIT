def mediani(lista):
    mediani=[]
    lunghezza=len(lista)
    mediani.append(lista[1:lunghezza-1])
    return mediani




if __name__ == '__main__':
    lista=[1,2,3,4,5,6]
    listaMediani=mediani(lista)
    print(listaMediani)
