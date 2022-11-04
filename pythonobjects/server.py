import socket
from product import Product

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((socket.gethostname(), 4567))
    python_dictionary = {'a': 1, 'b': 2}
    custom_object = Product('P012', 'Torch', 11)

    s.listen(5)
    print('Server is up')

    client, address = s.accept()
    print(client)
    print(address)

    client.send(bytes(str(python_dictionary),'utf-8'))
    client.send(bytes(str(custom_object),'utf-8'))
