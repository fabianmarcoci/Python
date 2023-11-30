import os
import sys

if __name__ == '__main__':
    directory_path = './workplace_script2'

    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        sys.exit(1)

    counter = 1
    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                extension = os.path.splitext(file)[1]
                new_filename = f"file{counter}{extension}"
                original_file = os.path.join(root, file)
                new_file = os.path.join(root, new_filename)
                if os.path.exists(new_file):
                    print(f"Cannot rename {file} to {new_filename} because it already exists.")
                    counter += 1
                    continue

                try:
                    os.rename(original_file, new_file)
                    print(f'Renamed "{file}" to "{new_filename}"')
                    counter += 1
                except PermissionError as e:
                    print(f"Permission denied for renaming {file}: {e}")
                except FileNotFoundError as e:
                    print(f"File not found: {file}")
                except OSError as e:
                    print(f"OS error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
    except PermissionError as e:
        print(f"Permission denied to list directory {directory_path}: {e}")
        sys.exit(1)
