def main():
    fin = open('words.txt')
    for i in fin:
        riga = fin.readline()
        parola=riga.split(" ")
        append2(parola)


#def append(stringa):
    #lista=[]
    #lista.append(stringa)
    #print(lista)

def append2(stringa):
    lista=[]
    lista=lista+[stringa]
    print(lista)

if __name__ == '__main__':
    main()