import socket
import threading
from util.file_handling import read, write
from util.binary_handling import string_to_binary, binary_to_string

def receive_messages():
    while True:
        try:
            response = client_socket.recv(1024).decode()
            # print('Received from server (Client A):', response)
            response = binary_to_string(response)
            write('./client_b_files/received_file.txt', response)
        except ConnectionResetError:
            break

def send_messages():
    while True:
        message = input("Client B: Enter a message to send (or 'exit' to quit): ") # input message to be sent

        client_socket.sendall(message.encode()) # send image to server

        if message == 'exit':
            break



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creting tcp/ip socket

server_address = ('localhost', 12345) # defining server adress and ports

client_socket.connect(server_address) # connecting to server

receive_thread = threading.Thread(target=receive_messages) # thread that receives messages
receive_thread.start()

send_thread = threading.Thread(target=send_messages) # thread that sends messages
send_thread.start()



receive_thread.join()
send_thread.join()

# Close the client socket
client_socket.close()