def tronca(lista):
    lista.pop(0)
    lista.pop(len(lista)-1)
    return lista




if __name__ == '__main__':
    lista=[1,2,3,4,5,6]
    listaTronca=tronca(lista)
    print(listaTronca)
