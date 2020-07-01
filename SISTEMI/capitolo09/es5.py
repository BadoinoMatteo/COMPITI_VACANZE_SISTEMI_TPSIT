def main():
    lettere= input("inserisci lettere da usare")
    parorla= input("inserisci parola")
    esito=usa_tuttte(parorla, lettere)
    print(esito)

def usa_tuttte(parola, lettere):
    for let in lettere:
        if let not in parola:
            return False
    return True

if __name__ == '__main__':
    main()