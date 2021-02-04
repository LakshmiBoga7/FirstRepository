import socket
import sys

SERVER_IP="127.0.0.1"
SERVER_PORT=1600
MAXSIZE=64

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clisock:
    clisock.connect((SERVER_IP, SERVER_PORT))

    mystr="Hello World"
    clisock.send(mystr.encode('utf-8'))
    data = clisock.recv(MAXSIZE)
    print("server sent back:",data.decode('utf-8'))


