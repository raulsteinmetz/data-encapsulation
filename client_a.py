import socket
import threading
from util.file_handling import read
from util.binary_handling import string_to_binary, binary_to_string

def receive_messages():
    while True:
        try:
            response = client_socket.recv(1024).decode()
            print('Received from server (Client B):', response)
        except ConnectionResetError:
            break

def send_messages():
    while True:
        print("Type the operation you want to perform:")
        print("1. Send a file to Client B")
        print("2. Exit")

        action = int(input("Client A: "))
        if action == 1:

            path = input("Client A: Type the path of the file you want to send: ")
            path = './client_a_files/' + path
            message = read(path)
            print(message)
            message = string_to_binary(message)

            # Send the message to the server
            client_socket.sendall(message.encode())
            
        elif action == 2:
            break

        else:
            pass



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating tcp/ip socket

server_address = ('localhost', 12345) # defining server adress and port

client_socket.connect(server_address) # connecting to server

receive_thread = threading.Thread(target=receive_messages) # thread that receives messages
receive_thread.start()

send_thread = threading.Thread(target=send_messages) # thread that sends messages
send_thread.start()

# waiting for both threads to finish
send_thread.join()
receive_thread.join()


client_socket.close() # close socket

