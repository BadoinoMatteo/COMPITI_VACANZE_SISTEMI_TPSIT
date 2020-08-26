import random

def main():
    h = istogramma('brontosauro')
    print(h)
    print (h[random.randint(0,len(h)-1)])

def istogramma(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

if __name__ == '__main__':
    main()