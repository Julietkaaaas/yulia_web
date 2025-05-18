from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('localhost', 12345))

print(client_socket.recv(1024).decode())

client_socket.close()