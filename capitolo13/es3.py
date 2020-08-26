import string

def main():
    dict= {}
    cont=0
    fin=open("estrattoLibro.txt")
    for i in fin:
        riga=i.strip(string.whitespace).lower()
        print(riga)
        parola=riga.split(' ')
        for i in parola:
            print(parola[i])
            chiave = str(parola[i])
            print(chiave)
            if chiave not in dict:
                dict[chiave]=1
            else:
                dict[chiave]+=1
            cont=cont+1
        print(dict)
        print(cont)
    min=5000
    lista=[20]
    for i in dict:
        if(dict[i]<min):
            lista.append(dict.keys())

    print(lista)


if __name__ == '__main__':
    main()