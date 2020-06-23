import socket
import threading


localIP= "127.0.0.1"
localPort= 80
lock=threading.Lock()
mex=""
listaClient=[]

def main():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((localIP, localPort))

    s.listen()
    conn, addr = s.accept()
    while True:
        mex=conn.recv(4096)
        thred = (threading.Thread(target=client(), args=mex))
        listaClient.append(thred)
        listaClient.start()

    for i, t in enumerate (listaClient):
        t.join()
    s.close()

def client():
    lock.acquire()
    print(mex)
    lock.release()

if __name__ == '__main__':
    main()