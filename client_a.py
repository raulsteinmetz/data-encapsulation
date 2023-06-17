import socket
import threading
from util.file_handling import read
from util.binary_handling import string_to_binary, binary_to_string
from frame import Frame
import time

SEND_FILE_PATH = './client_a_files/a.txt'

def receive_messages():
    while True:
        try:
            response = client_socket.recv(1024).decode()
            print('Received from server (Client B):', response)
        except ConnectionResetError:
            break

def send_messages():
    message = read(SEND_FILE_PATH)
    message = string_to_binary(message)

    # separating message into frames with 64 bits each
    id = 0
    for i in range(0, len(message), 8):
        frame = Frame(message[i:i+8], id)
        frame_list.append(frame)
        id += 1
    
    input("Press enter to send the message to the server...")

    # sending frames to the server in separate messages
    for frame in frame_list:
        client_socket.sendall(frame.data.encode())
        time.sleep(1)

    # Send the message to the server
    # client_socket.sendall(message.encode())



# main
frame_list = []

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

