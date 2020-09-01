import socket
import threading

localIP = "127.0.0.1"
localPort = 80
lock = threading.Lock()
mex = ""
listaClient = []


def main():
    listaClient = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((localIP, localPort))

    s.listen()
    while True:
        conn, addr = s.accept()
        #mex = conn.recv(4096)
        thread=threading.Thread(target=client, args=(conn, addr))
        thread.start()
        listaClient.append(thread)

    for i, t in enumerate(listaClient):
        t.join()

    s.close()


def client(conn, addr):
    mex=conn.recv(4096).decode()
    print(mex)



if __name__ == '__main__':
    main()
