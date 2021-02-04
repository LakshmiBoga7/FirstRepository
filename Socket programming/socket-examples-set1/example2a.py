import socket
import sys

SERVER_IP="127.0.0.1"
SERVER_PORT=1500
MAXSIZE=64

clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clisock.bind((SERVER_IP, SERVER_PORT))
clisock.connect((SERVER_IP, SERVER_PORT))

for x in range(1,4):
    mystr="Hello World"
    clisock.send(mystr.encode('utf-8'))
    data = clisock.recv(MAXSIZE)
    if not data : break
    print("server sent back:",data.decode('utf-8'))

clisock.close()
