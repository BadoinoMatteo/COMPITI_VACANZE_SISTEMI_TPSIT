def main():
    dict= {'a':1, 'b':2, 'c':3 }
    dictInvertito= invertiDict(dict)
    print(dict)
    print(dictInvertito)


def invertiDict(d):
    dictInvertito={}
    for i in d:
        val=d[i]
        dictInvertito.setdefault(val, []).append(i)
    return dictInvertito

if __name__ == '__main__':
    main()
