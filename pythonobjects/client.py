import socket
from product import Product

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(),4567))

    while True:
        msg = s.recv(1024)

        if not msg:
            print('Nothing received from server anymore')
            break
        print(msg.decode('utf-8'))
        print(type(msg))