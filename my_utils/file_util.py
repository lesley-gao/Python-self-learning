"""
These functions will be used in 08_package - package.py
"""

def print_file_info(file_dir):
    """
    Function to read and print the first line of a file.
    :param file_dir: The path of the file to be read.
    """
    try:
        with open(file_dir, "r", encoding="UTF-8") as file:  # Automatically closes the file when the block exits
            content = file.read()  # Read the first line of the file
            print(content)
    except FileNotFoundError:    # Handle the case where the file does not exist
        print("Oops! The file doesn't exist.")
    except Exception as e:       # Handle any other exceptions
        print(f"An error occurred: {e}")


def append_to_file(file_dir, data):
    """
    Function to append data to a file.
    :param file_dir: The path of the file to be written to.
    :param data: The data to append to the file.
    """
    try:
        # Open the file in append mode with UTF-8 encoding
        with open(file_dir, "a", encoding="UTF-8") as file:
            file.write(data)
    except FileNotFoundError:
        print("Oops! The file doesn't exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    print_file_info("D:/test.txt")
    append_to_file("D:/test.txt", "See you tomorrow!!!")
