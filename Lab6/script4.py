import sys
import os


def count_files_by_extension(directory_path):
    try:
        files = os.listdir(directory_path)
        if not files:
            print(f"The directory {directory_path} is empty.")
            return

        extensions_dict = {}
        for filename in files:
            if os.path.isfile(os.path.join(directory_path, filename)):
                extension = os.path.splitext(filename)[1].lower()
                extensions_dict[extension] = extensions_dict.get(extension, 0) + 1

        print(f"Count of files by extension in directory {directory_path}:")
        for ext, count in sorted(extensions_dict.items()):
            print(f"{ext if ext else 'no extension'}: {count}")

    except PermissionError:
        print(f"Permission denied: cannot access the directory {directory_path}")
    except FileNotFoundError:
        print(f"File not found: {directory_path} does not exist")
    except OSError as e:
        print(f"OS error: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Correct usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        sys.exit(1)

    count_files_by_extension(directory_path)
