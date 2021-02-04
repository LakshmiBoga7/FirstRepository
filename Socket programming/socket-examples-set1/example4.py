"""
UDP Receiver
"""
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"
MAX_SIZE = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data, addr = sock.recvfrom(MAX_SIZE)
print("received back message: {1}", data)
