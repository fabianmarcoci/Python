import sys
import os

# note: comments are only for me to understand the code when I come back to it
if __name__ == '__main__':
    # sys.argv[0] is the script name
    if len(sys.argv) != 3:
        print("Correct usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    if not file_extension.startswith('.'):
        print("The file extension should start with a dot. For example, use '.txt' instead of 'txt'.")
        sys.exit(1)

    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        sys.exit(1)

    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    print(f'{file_path} content:')
                    try:
                        # with ensures the file is properly closed after its content is read
                        with open(file_path, 'r') as content_file:
                            content = content_file.read()
                            print(content)
                    except PermissionError as e:
                        print(f"Permission denied for file {file_path}: {e}")
                    except FileNotFoundError as e:
                        print(f"File not found: {file_path}")
                    except OSError as e:
                        print(f"OS error for file {file_path}: {e}")
                    except Exception as e:
                        print(f"An unexpected error occurred for file {file_path}: {e}")
    except PermissionError as e:
        print(f"Permission denied to access directory {directory_path}: {e}")
        sys.exit(1)
