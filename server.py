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
        if data["command"] == "a":
            users.append(data["data"]["name"])
        elif data["command"] == "d":
            users.remove(data["data"]["name"])
        elif data["command"] == "all":
            connection.send(json.dumps(users).encode())
        elif data["command"] == "r":
            users = list(map(lambda x: x.replace(data["data"]["f_berry"], data["data"]["s_berry"]), users))

    except:
        server.close()
        break

