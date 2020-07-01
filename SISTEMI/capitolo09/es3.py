def main():
    carattereVietati = ""
    parola=""
    carattereVietati=input("inserisci la stringa di caratteri vietati")
    parola= input("inserisci stringa ")
    esito= evita(parola, carattereVietati)
    print(esito)


def evita(parola, cartVietati):
    i=0
    c=0
    while i < len(parola):
        while c<len(cartVietati):
            if parola[i] == cartVietati[c]:
                return False
            c = c + 1
        i=i+1

    return True


if __name__ == '__main__':
    main()