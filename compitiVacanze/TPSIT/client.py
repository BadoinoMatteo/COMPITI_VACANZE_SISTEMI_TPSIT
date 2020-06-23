import socket
import time

ip= "127.0.0.1"
porta = 80
message= ""

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip,porta))

message=input("inserisci il messaggio da inoltrare")
s.sendall(message.encode())

recv=s.recv(1024)

print(recv.decode())

s.close()