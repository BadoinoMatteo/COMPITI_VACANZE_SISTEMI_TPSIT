import string
def main():
    lista =[]
    fin = open('words.txt')
    for i in fin:
        riga=fin.readline()
        riga=riga.split('/n')
        print(riga)
        riga=riga.split(string.whitespace)
        if string.punctuation in riga:
            parola=riga.split(string.punctuation)
            lista.append(parola[0])
        else:
            lista.append(riga)
    print(lista)

if __name__ == '__main__':
    main()