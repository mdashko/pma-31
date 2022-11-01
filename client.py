
import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5050))


def add_drink():
    drink = dict()

    all_drinks = view_drinks()

    drink["id"] = int(input("Give drink id(int):"))
    drink["name"] = input("Give drink a name:")
    drink["volume"] = float(input("Give it a volume:"))

    header = "POST"+' '+ drink["id"]+"\n"

    body = json.dumps(drink)

    return client.send((header+body).encode("utf-8"))


def view_drinks():
    return client.send("GET all".encode("utf-8"))

def view_drink():

    drink = dict()

    drink["id"] = int(input("Give drink id(int):"))
    return client.send(f"GET {drink['id']}".encode("utf-8"))


def update_drink():
    
    drink = dict()

    all_drinks = view_drinks()

    drink["id"] = int(input("Give drink id(int):"))
    drink["name"] = input("Give drink a name:")
    drink["volume"] = float(input("Give it a volume:"))

    header = "POST"+' '+ drink["id"]+"\n"

    body = json.dumps(drink)

    return client.send((header+body).encode("utf-8"))

def delete_drink():
    drink = dict()

    all_drinks = view_drinks()

    drink["id"] = int(input("Give drink id(int):"))
    # drink["name"] = input("Give drink a name:")
    # drink["volume"] = float(input("Give it a volume:"))

    header = "DELETE"+' '+ drink["id"]+"\n"


    return client.send(header.encode("utf-8"))




while True:

    option = input("Type a method")

    if option == "Get drink":
        view_drink()
    elif option == "Get all drinks":
        view_drinks()
    elif option == "Update drink":
        update_drink()
    elif option == "Add drink":
        add_drink()
    elif option == "Delete drink":
        delete_drink()
    



