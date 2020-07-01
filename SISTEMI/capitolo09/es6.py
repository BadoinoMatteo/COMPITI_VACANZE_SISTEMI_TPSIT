def main():
    parola=input("inserisci parola")
    esito=alfabetica(parola)
    print(esito)

def alfabetica(parola):
    precedente=parola[0]
    for c in parola:
        if(c< precedente):
            return False
        precedente=c
    return True


if __name__ == '__main__':
    main()