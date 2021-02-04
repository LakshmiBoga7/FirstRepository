"""
UDP Sender
"""
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MAX_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(MAX_SIZE) 
    print("received message: {1} from {2}", data, addr)
    sock.sendto(data, addr)

sock.close()

