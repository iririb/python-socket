import socket
from product import Product
# serializing and deserializing a python object
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 4567))
    
    python_dictionary = {'a': 1, 'b': 2}
    pickled_dictionary = pickle.dumps(python_dictionary)

    custom_object = Product('P012', 'Torch', 11)
    pickled_object = pickle.dumps(custom_object)

    print(type(pickled_dictionary))
    print(type(pickled_object))

    s.listen(5)
    print('Server is up')

    client, address = s.accept()
    print(client)
    print(address)

    client.send(pickled_dictionary)
    # client.send(pickled_object)
