def main():
    parola=input("inserisci una parola")
    esito = niente_e(parola)
    print(esito)

def niente_e(parola):
    esito= False
    divisione=''
    divisione= parola.split('e')
    if(divisione[0]== '' or divisione[1] == ''):
        esito=True
    else:
        esito=False
        #i=i+1
    return esito

if __name__ == '__main__':
    main()