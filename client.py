import socket
import json

socket_server = socket.socket()

socket_server.connect(("127.0.0.1", 3000))

while True:
    try:
        data = {}
        command = input("Input command: ")
        if command == "new user" or command == "remove user":
            name = input("Username: ")
            data = {"command":command,"data":{"name":name}}
            socket_server.send(json.dumps(data).encode())

        elif command == "replace users":
            user_a = input("Input user a: ")
            user_b = input("Input user b: ")
            data = {"command":command,"data":{"user_a":user_a,"user_b":user_b}}
            socket_server.send(json.dumps(data).encode())

        elif command == "list users":
            data = {"command":command}
            socket_server.send(json.dumps(data).encode())
            users = socket_server.recv(1024)
            users = json.loads(users.decode())
            print("\n".join(users))

        else:
            print("incorrect command")
            print("available commands: new user, remove user, replace users, list users")
    except:
        socket_server.close()
        break