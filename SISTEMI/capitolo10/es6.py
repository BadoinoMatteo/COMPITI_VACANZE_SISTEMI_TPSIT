def anagramma(stringa1, stringa2):
    if sorted(stringa1) == sorted(stringa2):
        return True
    else:
        return False


if __name__ == '__main__':
    stringa1=input("inserisci una parola")
    stringa2=input("inserisci una parola")
    esito=anagramma(stringa1,stringa2)
    print(esito)