import socket
import threading
import random


BIT_ERROR_CHANCE = 0.1
BURST_ERROR_CHANCE = 0.1

class ChannelNoise():
    def __init__(self):
        self.burst_error_lenght = -1
        self.burst_error_counter = 0
        self.bit_error_chance = BIT_ERROR_CHANCE
        self.burst_error_chance = BURST_ERROR_CHANCE

    # implements bit error
    def bit_error(self, message):
        modified_message = message
        # randomize number between 0 and 1 
        random_number = random.random()
        
        if random_number < self.bit_error_chance:
            print('!!!bit error!!!')
            print('message:', message)
            # randomize position of bit to be flipped
            random_position = random.randint(0, len(message) - 1)
            # flip bit
            message_list = list(message)
            message_list[random_position] = '1' if message_list[random_position] == '0' else '0'
            modified_message = "".join(message_list)
            print('noise affected message:', modified_message)

        return modified_message


    # implements burst error
    def burst_error(self, message):
        random_number = random.random()
        initial_position = 0
        if (random_number < 0.1):
            self.burst_error_lenght = 10
            self.burst_error_counter = 0
            print('!!!burst error!!!')
            print('burst error lenght:', self.burst_error_lenght)

            initial_position = random.randint(0, len(message) - 1)

        if self.burst_error_counter < self.burst_error_lenght:
            print('message:', message)
            for i in range(initial_position, len(message)):
                if self.burst_error_counter == self.burst_error_lenght:
                    break

                message_list = list(message)
                message_list[i] = '1' if message_list[i] == '0' else '0'
                message = "".join(message_list)
                self.burst_error_counter += 1

            print('noise affected message:', message)
        return message
        

        

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

                # message = channel_noise.bit_error(message)
                message = channel_noise.burst_error(message)

                # forwarding message to the other client
                if self == client_A:
                    client_B.client_socket.sendall(message.encode())
                else:
                    client_A.client_socket.sendall(message.encode())

            except ConnectionResetError:
                break

        self.client_socket.close()


channel_noise = ChannelNoise()

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
