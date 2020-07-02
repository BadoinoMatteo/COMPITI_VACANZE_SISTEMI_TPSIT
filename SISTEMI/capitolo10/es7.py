def haDuplicati(lista):
    l = list(lista)
    l.sort()
    for i in range (len(l)-1):
        if l[i]==l[i+1]:
            return True
    return False


if __name__ == '__main__':
    lista=[1,2,3,4,4]
    esito=haDuplicati(lista)
    print(esito)