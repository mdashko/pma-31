import socket

socket_server = socket.socket()

name = input("Введіть ім'я: ")
socket_server.connect(("127.0.0.1",50))
socket_server.send(name.encode())
socket_name = socket_server.recv(1024)
server_name = socket_name.decode()
print(server_name, " приєдналася!")

while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name,":",message)
    message = input("Я: ")
    socket_server.send(message.encode())
    
