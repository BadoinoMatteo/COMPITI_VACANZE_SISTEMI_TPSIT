import random
import bisect
def main():
    fin=open('estrattoLibro.txt', 'r')
    parole=[]
    freq=[]
    totFreq=0
    for i in fin:
        parola=i.split(' ')
        if(parola in parole):
            freq[parola]+=1
        else:
            parole.append(parola)
        totFreq+=1

    x=random.randint(0, totFreq-1)
    index=bisect.bisect(freq, x)
    print(parole[index])




if __name__ == '__main__':
    main()