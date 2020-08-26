def main():
    lista=[]
    bifronte=[]
    fin=open("words.txt")
    for i in fin:
        riga = fin.readline()
        parola=riga.split(" ")
        lista.append(parola)
        print(parola)
    print(lista)
    for i in lista:
        if(i ==invertiparola(parola)):
            bifronte.append(parola)
    print(bifronte)

def invertiparola(stringa):
    return stringa[::-1]

if __name__ == '__main__':
    main()