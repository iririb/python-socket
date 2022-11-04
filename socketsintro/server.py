import socket

# initializing socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind a socket to particular address
s.bind((socket.gethostname(),4567))

# wait to establish connection, if no connection establish throw an error
s.settimeout(10)

try:
    # invoke the socket
    # can received up to 5 connection
    s.listen(5)

    print('Server is up. Listening for connections...')

    # once recieved client request
    client, address = s.accept()
    print('Conection to ',address, ' has been established\n')
    print('Client object:',client,'\n')

    # sending the data to client, need to send in bytes
    msgFromServer = bytes('Hello! Welcome to socket programming.','utf-8')
    client.send(msgFromServer)

    # need to close once no longer required
    s.close()

except socket.timeout:    
    print('Timeout exceeded')
    