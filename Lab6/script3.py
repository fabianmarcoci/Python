import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Correct usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        sys.exit(1)

    bytes_sum = 0
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(file_path)
                    bytes_sum += size
                except PermissionError as e:
                    print(f"Permission denied for file {file_path}: {e}")
                except FileNotFoundError as e:
                    print(f"File not found: {file_path}")
                except OSError as e:
                    print(f"OS error for file {file_path}: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred for file {file_path}: {e}")
    except PermissionError as e:
        print(f"Permission denied to list directory {directory_path}: {e}")
        sys.exit(1)

    print(f"Total size of files in directory {directory_path} is: {bytes_sum} bytes")
