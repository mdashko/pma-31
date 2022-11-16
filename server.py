import socket

s = socket.socket()
print("Socket successfully created")

port = 12345

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")

c, addr = s.accept()
print('Got connection from', addr)
while True:
    data = c.recv(1024).decode()
    if not data:
        break
    print("from connected user: " + str(data))
    data = input('... ')
    c.send(data.encode())


c.send('Thank you for connecting'.encode())
c.close()
