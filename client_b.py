import socket
import threading
from util.file_handling import read, write
from util.binary_handling import string_to_binary, binary_to_string
from frame import Frame, FrameList


def receive_messages():
    while True:
        try:
            frame = client_socket.recv(1024).decode()
            print('Received from server (Client A):', frame)

            # adding message to frame list
            frame_list.add_frame_by_frame(frame)
            
        except ConnectionResetError:
            break

def send_messages():
    while True:
        message = input("Client B: Enter 'save' to save message received: ") # input message to be sent

        if message == 'save':
            # writing frames to file
            # create a string with all frames
            message = ''
            for frame in frame_list.frame_list:
                message += frame.data
            
            # converting binary string to string
            message = binary_to_string(message)
            print(message)
            # saving
            write('./client_b_files/received_file.txt', message)

            break


# main

frame_list = FrameList()


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