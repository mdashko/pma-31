"""
Server part of a project
"""

# Importing libraries
import socket
import json
import string


class Server:

    def __init__(self, host = "127.0.0.1", port = 5050, listen = 100) -> None:
        self.__host = host
        self.__port = port
        self.__listen = listen

        self.__drinks = dict()


    def run(self):
        
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
            server_socket.bind((self.__host, self.__port))
            server_socket.listen(self.__listen)
    
            while True:
                client_socket, _ = server_socket.accept()
                message = client_socket.recv(1028).decode("utf-8")
                client_socket.send(self.call_route(message).encode("utf-8"))       
                client_socket.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            print("Shutting server down...")
        finally:
            server_socket.close()     

    def parse_message(self, message):

        if message == "":
            elements = message.split(" ")
            return [elements[0], elements[1]]


    def call_route(self, message):
        method, drink_id = self.parse_message(message)

        if method == "GET" and drink_id == "all":
            response = self.create_response(self.__drinks)

        elif str.isdigit(drink_id):
            
            drink_id = int(drink_id)

            if method == "GET":

                if self.__drinks:
                    response = self.create_response(self.__drinks[drink_id])
                else: 
                    response = self.create_response(self.__drinks)


            elif method == "POST":
                drink = json.loads(message.split('\n')[1])
                
                self.__drinks[drink_id] = drink

                response = self.create_response(self.__drinks)

            elif method == "PUT":
                drink = json.loads(message.split('\n')[1])

                if drink_id in self.__drinks.keys():
                    self.__drinks[drink_id] = drink
                
                response = self.create_response(self.__drinks)

            elif method =="DELETE":

                if drink_id in self.__drinks.keys():
                    del self.__drinks[drink_id]

                response = self.create_response(self.__drinks)
            
        else:
            response = self.create_response(self.__drinks)

        return response


    def create_response(self,reason):
        
        # status_code = 200
        # content_type = "application/json"

        # headers = "".join([
        #     f"HTTP/1.1 {status_code} OK\r\n",
        #     f"Accept: {content_type};\r\n",
        #     f"Access-Control-Allow-Origin: *\r\n",
        #     f"Content-Type: {content_type}; charset=utf-8;\r\n\r\n"
        # ])

        return json.dumps(reason)

        
s = Server()
s.run()