import random

def main():
    listaDate=[23]
    cont=0
    for i in range (0,23):
        listaDate.append(random.randint(1,31))
    print(listaDate)
    if(haDuplicati(listaDate)):
        cont+=1
    probabilita=cont/23*100
    print(probabilita)


def haDuplicati(lista):
    l = list(lista)
    l.sort()
    print(l)
    for i in range (len(l)-1):
        if l[i]==l[i+1]:
            return True
    return False







if __name__ == '__main__':
    main()