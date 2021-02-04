import socket
import sys

SERVER_IP="127.0.0.1"
SERVER_PORT=1500
MAXSIZE=64

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.bind((SERVER_IP, SERVER_PORT))
    server_sock.listen(3)

    (client, addr) = server_sock.accept() 
    with client  :
        print("Received a connection from", addr)
        while True:
            data = client.recv(MAXSIZE)
            if not data :
                break
            print("client says :", data.decode('utf-8'))
            client.send(data)
    

