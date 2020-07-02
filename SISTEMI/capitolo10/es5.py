def ordinata(lista):
    if sorted(lista)==lista:
        esito=True
    else:
        esito=False
    return esito


if __name__ == '__main__':
    lista=[1,2,3,4,5]
    esito=ordinata(lista)
    if(esito==True):
        print("la lista è ordinata")
    else:
        print("la lista non è ordinata")