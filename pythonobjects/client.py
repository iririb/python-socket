import socket
from product import Product
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), 4567))

    while True:
        msg = s.recv(1024)

        if not msg:
            print('Nothing received from server anymore')
            break
        
        product_object = pickle.loads(msg)
        print(product_object.pid)
        print(product_object.pname)
        print(product_object.pprice)