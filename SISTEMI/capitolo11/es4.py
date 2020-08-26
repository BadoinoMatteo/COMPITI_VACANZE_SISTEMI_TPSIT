def main():
    dict={'a':1, 'b':2, 'c':3}
    esito=duplicati(dict)
    print(esito)

def duplicati(dict):
    duplicati=False
    i=0
    while duplicati== False and i<len(dict):
        if i in dict:
            duplicati=True
    return duplicati
if __name__ == '__main__':
    main()