import socket as sk

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
sock.setsockopt(sk.SOL_SOCKET, sk.SO_BROADCAST, 1)

while 1:
    message = input("введите сообщение: ")
    sock.sendto(message.encode("UTF-8"), ('0.0.0.0', 11719))
    