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

                if message == 'exit':
                    break

                # Forward the message to the other client
                if self == client_A:
                    client_B.client_socket.sendall(message.encode())
                else:
                    client_A.client_socket.sendall(message.encode())

            except ConnectionResetError:
                break

        self.client_socket.close()

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Bind the socket to the server address and port
server_socket.bind(server_address)

# Listen for incoming connections (maximum 2 connections)
server_socket.listen(2)

print('Server is running and listening for incoming connections...')

# Accept Client A connection
client_A_socket, client_A_address = server_socket.accept()
print('Client A connected:', client_A_address)

# Accept Client B connection
client_B_socket, client_B_address = server_socket.accept()
print('Client B connected:', client_B_address)

# Create client threads
client_A = ClientThread(client_A_socket, client_A_address)
client_B = ClientThread(client_B_socket, client_B_address)

# Start the client threads
client_A.start()
client_B.start()
