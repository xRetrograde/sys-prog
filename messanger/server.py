import socket
from sys import platform

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0', 11719))
#server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while 1:
    message = s.recv(128)
    print(f'{platform} >> {message.decode("utf-8")}')
