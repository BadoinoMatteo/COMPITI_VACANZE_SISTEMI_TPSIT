
def main():
    fin=open('words.txt')
    for i in fin:
        parola= fin.readline()
        esito= niente_e(parola)
        print(parola + " ")
        print(esito)

def niente_e(Stringa):
    Indice = 0
    while Indice < len(Stringa):
        if Stringa[Indice] == 'e':
            return True
    Indice = Indice + 1
    return False


if __name__ == '__main__':
    main()