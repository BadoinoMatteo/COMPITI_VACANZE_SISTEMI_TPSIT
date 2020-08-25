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
        #parola.upper()
        #print(parola)


if __name__ == '__main__':
    main()