def string_to_binary(string):
    binary = ""
    for char in string:
        binary += bin(ord(char))[2:].zfill(8)  # Convert character to ASCII and then to binary
    return binary

def binary_to_string(binary):
    string = ""
    for i in range(0, len(binary), 8):
        binary_byte = binary[i:i+8]
        decimal = int(binary_byte, 2)
        string += chr(decimal)  # Convert binary to decimal and then to character
    return string
