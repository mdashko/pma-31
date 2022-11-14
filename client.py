import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((socket.gethostname(), 1234))

msg = server.recv(1024)
print(msg.decode('utf-8'))