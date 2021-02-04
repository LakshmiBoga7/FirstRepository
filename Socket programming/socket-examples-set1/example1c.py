import socket
import sys

SERVER_IP="127.0.0.1"
SERVER_PORT=1500
MAXSIZE=64

class TcpServer:
    def __init__(self,ipaddr,port):
        self.addr=ipaddr
        self.port=port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.addr, self.port))
        self.sock.listen()

    def accept(self):
        client, addr = self.sock.accept()
        print("Received a connection from", addr)
        self.client = client

    def mysend(self, mystr):
        self.client.send(mystr.encode('utf-8'))
        
    def myrecv(self):
        data = self.client.recv(MAXSIZE)
        if not data: return None
        return data.decode('utf-8')
            
    def __del__(self):
        self.sock.close()
        
if __name__ == "__main__":
    server = TcpServer("127.0.0.1",1600)
    server.accept()
    while True:
        mystr = server.myrecv()
        if mystr == None : break
        server.mysend(mystr)
    

