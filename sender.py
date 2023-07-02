import socket
import threading
from util.file_handling import read
from util.binary_handling import string_to_binary, binary_to_string
from frame import Frame, FrameList
import time
import crc

SEND_FILE_PATH = './client_a_files/a.txt'

# criar uma classe sender que controla o envio de frames
class Sender:
    def __init__(self, frame_list):
        self.frame_list = frame_list
        self.window_size = 8
        self.window_start = 0

def receive_messages():
    while True:
        try:
            response = client_socket.recv(1024).decode()
            print('Confirmation from receiver:', response)

        except ConnectionResetError:
            break

def send_messages():
    message = read(SEND_FILE_PATH)
    message = string_to_binary(message)

    # separating message into frames with 32 bits each
    for i in range(0, len(message), 24):
        message_to_be_added = message[i:i+24]
        message_to_be_added = crc.generate_crc(message_to_be_added, crc.crc_polynomium)
        frame_list.add_frame_by_message(message_to_be_added)
    
    input("Press enter to send the message to the server...")

    sender = Sender(frame_list)

    # sending frames to the server in separate messages
    for frame in frame_list.frame_list:
        client_socket.sendall(frame.entire_frame.encode())
        time.sleep(0.01)
        # aqui tem que fazer o sistema da janela do n arq




# main
frame_list = FrameList()

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

