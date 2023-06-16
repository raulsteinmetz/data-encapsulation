def read(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")


def write(file_path, file_contents):
    try:
        with open(file_path, 'w') as file:
            file.write(file_contents)
    except IOError:
        print(f"Error writing to file '{file_path}'.")


