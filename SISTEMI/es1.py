def main():
    dict={}
    fin = open('words.txt')
    for i in fin:
        riga = fin.readline()
        dict.setdefault(riga)
    print(dict)
    print("\n")


if __name__ == '__main__':

    main()