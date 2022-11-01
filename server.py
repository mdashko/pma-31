import socket
import json

server = socket.socket()
server.bind(("127.0.0.1", 3000))
server.listen()

print("Server is running...")
connection, address = server.accept()
users = []

while True:
    try:
        data = connection.recv(1024)
        data = json.loads(data.decode())
        if data["command"] == "new user":
            users.append(data["data"]["name"])
        elif data["command"] == "remove users":
            users.remove(data["data"]["name"])
        elif data["command"] == "list users":
            connection.send(json.dumps(users).encode())
        elif data["command"] == "replace user":
            users = list(map(lambda x: x.replace(data["data"]["user_a"], data["data"]["user_b"]), users))

    except:
        server.close()
        break
