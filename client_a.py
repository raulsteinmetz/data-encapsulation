import socket
import threading

def receive_messages():
    while True:
        try:
            response = client_socket.recv(1024).decode()
            print('Received from server (Client B):', response)
        except ConnectionResetError:
            break

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect the socket to the server address and port
client_socket.connect(server_address)

# Start a thread to receive and display messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    # Get user input to send a message
    message = input("Client A: Enter a message to send (or 'exit' to quit): ")

    # Send the message to the server
    client_socket.sendall(message.encode())

    if message == 'exit':
        break

# Close the client socket
client_socket.close()

