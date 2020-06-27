def main():
    carattereObbligatori = ""
    parola=""
    carattereObbligatori=input("inserisci la stringa di caratteri obblogatori")
    parola= input("inserisci stringa ")
    esito= evita(parola, carattereObbligatori)
    print(esito)


def evita(parola, cartObbligatori):
    i=0
    c=0
    while i < len(parola):
        while c<len(cartObbligatori):
            if parola[i] == cartObbligatori[c]:
                esito= True
            else:
                return False
            c = c + 1
        i=i+1
    if(esito==True):
        return True
    else:
        return False


if __name__ == '__main__':
    main()