import socket

# initializing socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to running socket
s.connect((socket.gethostname(),4567))

msg = s.recv(1024)
print('Message from server:',msg.decode('utf-8'))

s.close()