def main():
    fin = open('words.txt')
    for i in fin:
        riga = fin.readline()
        esito=controllo(riga)
        if(esito==True):
            print(riga)

def controllo(parola):
    cont=0
    i=0
    while i <len(parola)-1:
        if(parola[i]==parola[i+1]):
            cont=cont+1
            if(cont==3):
                return True
            else:
                i=i+2
        else:
            i = i + 1 - 2 * cont
            cont=0

if __name__ == '__main__':
    main()