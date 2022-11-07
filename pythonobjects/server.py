import socket
from product import Product
# serializing and deserializing a python object
import pickle
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 4567))

    custom_objects = [Product('P022','Torch',13),
                      Product('P033','Pet bottle',12),
                      Product('P044','Mouse',11),
                      Product('P055','Keyboard',10)]

    s.listen(5)
    print('Server is up')

    client, address = s.accept()
    print(client)
    print(address)
    
    # looping for object send
    for product in custom_objects:
        pickled_product = pickle.dumps(product)
        client.send(pickled_product)
        print('Sent product:',product.pid)
        time.sleep(2)
