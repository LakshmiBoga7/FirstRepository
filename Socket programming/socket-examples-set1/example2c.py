import socket
import sys

SERVER_IP="127.0.0.1"
SERVER_PORT=1600
MAXSIZE=64

class TcpClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self,ipaddr, port):
        self.sock.connect((SERVER_IP, SERVER_PORT))
    
    def mysend(self, mystr):
        self.sock.send(mystr.encode('utf-8'))
        
    def myrecv(self):
        data = self.sock.recv(MAXSIZE)
        if not data: return None
        return data.decode('utf-8')
        
    def __del__(self):
        self.sock.close()
        
if __name__ == "__main__":
    client = TcpClient()
    client.connect(SERVER_IP, SERVER_PORT)
    client.mysend("Hello World")
    mystr = client.myrecv()
    print("server sent back:",mystr)
    
