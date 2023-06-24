def compare_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        content1 = file1.read()
        content2 = file2.read()

        if content1 == content2:
            print("The contents of the files are equal.")
        else:
            print("The contents of the files are not equal.")

# Example usage
file1_path = './client_a_files/a.txt'  # Replace with the actual path of file1
file2_path = './client_b_files/received_file.txt'  # Replace with the actual path of file2

compare_files(file1_path, file2_path)
