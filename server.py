import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                print('Received from', self.client_address, ':', message)

                # forwarding message to the other client
                if self == client_A:
                    client_B.client_socket.sendall(message.encode())
                else:
                    client_A.client_socket.sendall(message.encode())

            except ConnectionResetError:
                break

        self.client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating tcp/ip socket

server_address = ('localhost', 12345) # defining server adress and port

server_socket.bind(server_address) # binding the socket to the server address and port

server_socket.listen(2) # listening for incoming connections

print('Server is running and listening for incoming connections...')

# client a connection acceptance
client_A_socket, client_A_address = server_socket.accept()
print('Client A connected:', client_A_address)

# client b connection acceptance
client_B_socket, client_B_address = server_socket.accept()
print('Client B connected:', client_B_address)

# client socket threads 
client_A = ClientThread(client_A_socket, client_A_address)
client_B = ClientThread(client_B_socket, client_B_address)

# starting the client threads
client_A.start()
client_B.start()
