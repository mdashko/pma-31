import socket

new_socket = socket.socket()
new_socket.bind(("127.0.0.1",50))
new_socket.listen()

print("Сервер запущений!")
name = input("Введіть своє ім'я: ")
conn, add = new_socket.accept()

client = (conn.recv(1024)).decode()
print(client + ' приєднався!')
conn.send(name.encode())

while True:
    message = input('Я: ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client,':',message)
    
