import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# bind the socket to a public host and a well-known port
server_socket.bind((host, 9999))

# listen for incoming connections
server_socket.listen(1)

# wait for a connection
print('Waiting for a connection...')
client_socket, addr = server_socket.accept()

# print the address of the client
print('Connection from:', addr)

# send a message to the client
message = 'Thank you for connecting'
client_socket.send(message.encode('ascii'))

# close the connection
client_socket.close()