def main():
    fin = open('words.txt')
    for i in fin:
        riga = fin.readline()
        if (len(riga)>20):
            print(riga + "\n")



if __name__ == '__main__':
    main()