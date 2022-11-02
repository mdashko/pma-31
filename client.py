import socket
import json

sock = socket.socket()

sock.connect(("127.0.0.1", 3000))
print("Input a-add berry, d-delete berry, r-replace berry, all- all Kompot")
while True:
    try:
        data = {}
        command = input("Input command: ")
        if command == "a" or command == "d":
            name = input("Berry: ")
            data = {"command":command,"data":{"name":name}}
            sock.send(json.dumps(data).encode())

        elif command == "r":
            f_berry = input("Input first berry: ")
            s_berry = input("Input second berry: ")
            data = {"command":command,"data":{"f_berry":f_berry,"s_berry":f_berry}}
            sock.send(json.dumps(data).encode())

        elif command == "all":
            data = {"command":command}
            sock.send(json.dumps(data).encode())
            users = sock.recv(1024)
            users = json.loads(users.decode())
            print("\n".join(users))

        else:
            print("incorrect command")
    except:
        sock.close()
        break



