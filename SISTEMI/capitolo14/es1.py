def main():
    fin= open('source', 'r')
    out=open('dest', 'w')
    old="ciao"
    new="hello"
    sed(fin,out, old, new)

def sed(fin,out, old,new):
    for i in fin:
        line=i.replace(old,new)
        out.write(line)








if __name__ == '__main__':
    main()