import socket

s = socket.socket()

port = 12345

# connect to the server
s.connect(('127.0.0.1', port))

# receive data
message = input("...")
while message.lower().strip() != '':
        s.send(message.encode())
        data = s.recv(1024).decode()

        print('Received from server: ' + data)

        message = input("... ")
s.close()

