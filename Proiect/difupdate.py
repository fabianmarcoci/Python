import sys
import os


def check_file(file_name):
    """
        Verifies if a given file name corresponds to an existing file and not a directory.
        If the file does not exist, it attempts to create it with no content.
        If the file name corresponds to an existing directory, it prints an error message and returns None.
        If the file exists or is created successfully, it returns the file name.

        Parameters:
        file_name (str): The name of the file to check or create.

        Returns:
        str or None: The file name if the file exists or is created successfully, or None if there
        is a directory with the same name.
    """
    if not os.path.isfile(file_name):
        print(f"{file_name} does not exist. Creating the file.")
        try:
            with open(file_name, 'x'):
                pass
        except FileExistsError:
            print(f"A directory with the name {file_name} already exists.")
            return None
        return file_name
    else:
        return file_name


def try_open_file_read_bin(file_path):
    """
        Attempts to open a file in binary read mode. If successful, reads the entire
        content of the file and returns it. The function appends a '.bak' extension
        to the file path before attempting to open it. If the file cannot be opened
        or read due to various exceptions such as file not being found, permission
        errors, or other OS-related errors, the function will print an error message
        and return None.

        Parameters:
        file_path (str): The path of the file to be opened and read.

        Returns:
        bytes or None: The content of the file as a bytes object if the file was
        opened and read successfully; otherwise, returns None.
    """
    ext = '.bak'
    file_path += ext
    try:
        with open(file_path, 'rb') as file:
            file_contents = file.read()
            return file_contents
    except PermissionError as e:
        print(f"Permission denied for file {file_path}: {e}")
        return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except OSError as e:
        print(f"OS error for file {file_path}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred for file {file_path}: {e}")
        return None


def compute_difference(pre_version_file, latest_version_file):
    """
        Computes the differences between two versions of a file: a specified 'pre_version_file'
        and the 'latest_version_file'. The function performs a byte-wise comparison and produces
        a set of instructions indicating how to modify the 'pre_version_file' to match the
        'latest_version_file'. The instructions are returned as a UTF-8 encoded bytes object.

        The function first attempts to read both files in binary mode. If either file cannot
        be read, the program will exit with status code 1, indicating a critical error since
        the differences cannot be computed without both files.

        Each file's content is converted into a list of bytes to facilitate comparison and modification.
        The index of the version is extracted from the name of 'pre_version_file' to tag the
        instructions with the correct version number in the resulting diff.

        The '#' character is used as a marker in the 'abc.diff' file to differentiate between
        version indices and the actual data.

        The algorithm iterates through both versions:
        - If it encounters differing bytes, it appends a 'c' (change) followed by the differing byte and its index.
        - It then checks if the file lengths differ; if so, it appends an 'i' (insert) or 'd' (delete) command
          depending on whether the 'pre_version_file' is shorter or longer, respectively.

        An 'i' command is followed by the bytes to be inserted, each separated by a '|'.
        A 'd' command is followed by a series of '1' bits, equal in number to the length difference.

        The 'difference' list, which stores the instructions, is then joined into a single string
        and encoded into bytes using UTF-8.

        Parameters:
        pre_version_file (str): The path to the version file to compare against the latest version.
        latest_version_file (str): The path to the latest version file.

        Returns:
        bytes: The set of instructions for updating 'pre_version_file' to 'latest_version_file',
        encoded as a UTF-8 bytes object.
    """
    pre_version_file_content = try_open_file_read_bin(pre_version_file)
    if pre_version_file_content:
        pre_version = list(pre_version_file_content)
    else:
        sys.exit(1)

    latest_version_file_content = try_open_file_read_bin(latest_version_file)
    print(latest_version_file_content)
    if latest_version_file_content:
        latest_version = list(latest_version_file_content)
    else:
        sys.exit(1)
    ver_index = pre_version_file[-1]
    difference = ['#', ver_index]
    must_use_change = False
    print(latest_version)
    for i in range(min(len(pre_version), len(latest_version))):
        if pre_version[i] != latest_version[i]:
            if not must_use_change:
                difference.append('c')
                must_use_change = True
            difference.append(latest_version[i])
            difference.append('|')
            difference.append(i)
            difference.append('|')

    is_pre_version_smaller = False
    if len(pre_version) != len(latest_version):
        if len(pre_version) < len(latest_version):
            is_pre_version_smaller = True
            difference.append('i')
        else:
            difference.append('d')

        pre_version_size = len(pre_version)
        latest_version_size = len(latest_version)

        while pre_version_size != latest_version_size:
            if is_pre_version_smaller:
                difference.append(latest_version[pre_version_size])
                difference.append('|')
                pre_version_size += 1
            else:
                difference.append(1)
                pre_version_size -= 1

    difference_string = ''.join(map(str, difference))
    difference_bytes = difference_string.encode('utf-8')
    return difference_bytes


def create_bin(arg_files):
    """
        Processes a list of file paths to create a binary diff file 'abc.diff.bak'. The list should be sorted prior
        to calling this function, ensuring that 'abc.latest' is at index 0. This function iterates over the remaining
        file paths, computes their differences with the latest file using the 'compute_difference' function, and
        writes these differences to the diff file.

        If 'abc.latest' is not the first file, the script will exit with an error message.

        Parameters:
        arg_files (list of str): A list of file paths, where the first path should be 'abc.latest',
        and the remaining paths are the version files to compare against 'abc.latest'.

        Returns:
        None: This function does not return a value but writes the results to 'abc.diff.bak'.
        If an error occurs during file operations, an appropriate error message is printed, and the script exits.

        Raises:
        SystemExit: If 'abc.latest' is not the first file in 'arg_files',
         or if an unexpected error occurs during file handling.
    """
    if arg_files[0] != 'abc.latest':
        print('Script command should contain abc.latest file')
        sys.exit(1)

    file_path = 'abc.diff.bak'
    diff_file = check_file(file_path)

    try:
        with open(diff_file, 'wb') as file:
            for i in range(1, len(arg_files)):
                difference = compute_difference(arg_files[i], arg_files[0])
                print(f'Difference: {difference}')
                file.write(difference)
    except PermissionError as e:
        print(f"Permission denied for file {file_path}: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except OSError as e:
        print(f"OS error for file {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for file {file_path}: {e}")


def apply_commands(now_version_file, diff_file):
    """
          Applies transformation commands from a diff file to a target version file to reconstruct the latest version.
          The function reads the contents of the target version file and the diff file, expecting the diff file to
          contain a sequence of change (c), insertion (i), and deletion (d) commands specific to the version file's
          index.

          The changes are applied sequentially based on the commands found after the version index in the diff file.
          For changes, it replaces the byte at the specified index with a new value. For insertions, it adds the new
          value to the end of the file. For deletions, it removes the last byte from the file.
          The `enabled_insertion`, `enabled_delete`, and `enabled_change` flags can be True one at a time and dictate
          the current operation to be performed: replacing a byte for changes, appending a new byte for insertions,
          or removing the last byte for deletions.

          The process begins by identifying the start position of the relevant commands in the diff file by locating the
          version index preceded by the '#' marker. If no commands are found for the specified version,
          the script exits.

          After applying all the commands, the modified version is re-encoded into UTF-8 bytes
          to reflect the latest version.

          Parameters:
          now_version_file (str): The path to the target version file that needs to be updated.
          diff_file (str): The path to the diff file containing the commands.

          Returns:
          bytes: The reconstructed latest version of the file, encoded in UTF-8.

          Raises:
          SystemExit: If the diff file does not contain information for the given version, or if an error occurs during
          file reading.
      """
    now_version_file_content = try_open_file_read_bin(now_version_file)
    if now_version_file_content:
        now_version = list(now_version_file_content.decode('utf-8'))
    else:
        sys.exit(1)

    diff__file_content = try_open_file_read_bin(diff_file)
    if diff__file_content:
        diff = list(diff__file_content.decode('utf-8'))
    else:
        sys.exit(1)

    ver_index = now_version_file[-1]
    start_pos = None
    for i in range(1, len(diff)):
        if diff[i] == ver_index and diff[i - 1] == '#':
            start_pos = i

    if not start_pos:
        print(f'abc.diff doesnt contain any information about version {now_version_file}')
        sys.exit(1)

    enabled_insertion = False
    enabled_delete = False
    enabled_change = False
    j = 0
    for i in range(start_pos, len(diff)):
        # jump over evaluated characters
        if j > i:
            continue
        if diff[i] == '#':
            break
        if diff[i] == 'c':
            enabled_insertion = False
            enabled_delete = False
            enabled_change = True
            continue
        if diff[i] == 'i':
            enabled_insertion = True
            enabled_delete = False
            enabled_change = False
            continue
        if diff[i] == 'd':
            enabled_insertion = False
            enabled_delete = True
            enabled_change = False
            continue

        if enabled_change:
            j = i
            str_element = []
            # element extract
            while diff[j] != '|':
                str_element.append(diff[j])
                j += 1
            # pass '|' character
            j += 1
            str_element = ''.join(map(str, str_element))
            element = int(str_element)
            # index extract
            str_index = []
            while diff[j] != '|':
                str_index.append(diff[j])
                j += 1
            j += 1
            str_index = ''.join(map(str, str_index))
            index = int(str_index)
            now_version[index] = chr(element)
            print(f'Change | Current version is: {now_version}')
        elif enabled_insertion:
            j = i
            str_element = []
            # element extract
            while diff[j] != '|':
                str_element.append(diff[j])
                j += 1
            # pass '|' character
            j += 1
            str_element = ''.join(map(str, str_element))
            element = int(str_element)
            now_version.append(chr(element))
            print(f'Insert | Current version is: {now_version}')
        elif enabled_delete:
            now_version.pop(-1)
            print(f'Delete | Current version is: {now_version}')

    now_version_string = ''.join(map(str, now_version))
    now_version_bytes = now_version_string.encode('utf-8')
    return now_version_bytes


def update_bin(arg_files):
    """
        Updates a specific version of a file to the latest version using the rules defined within a diff file.
        The list of file paths must be sorted prior to calling this function to ensure that the diff file ('abc.diff')
        is at index 0 and the target version file ('abc.verx') is at index 1.
        The function applies the transformation commands found in 'abc.diff' to the target version file to reconstruct
        the latest version. The result is written to 'abc.latest.bak'.

        The function enforces the order of the files by checking the first element of the 'arg_files' list.
        If the order is incorrect, it prints an error message and exits the script.
        This function relies on 'apply_commands' to interpret and apply the instructions contained in the
        diff file to the target version file.

        Parameters:
        arg_files (list of str): A list containing the paths of the diff file and the target version file. The diff file
        must be the first element ('abc.diff'), followed by the target version file ('abc.verx').

        Returns:
        None: The function writes the updated file content to 'abc.latest.bak' and does not return a value. If any file
        operations fail, an error message is printed, and the script terminates.

        Raises:
        SystemExit: If the diff file ('abc.diff') is not the first element in 'arg_files', or if an unexpected error
        occurs during the file update process.
    """
    if arg_files[0] != 'abc.diff':
        print('Script command should contain abc.diff file')
        sys.exit(1)

    file_path = 'abc.latest.bak'
    latest_file = check_file(file_path)

    try:
        with open(latest_file, 'wb') as file:
            complete_version = apply_commands(arg_files[1], arg_files[0])
            file.write(complete_version)
    except PermissionError as e:
        print(f"Permission denied for file {file_path}: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except OSError as e:
        print(f"OS error for file {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred for file {file_path}: {e}")
    return


if __name__ == '__main__':
    """
            Entry point of the script. Validates command-line arguments and sorts the provided file paths.
            Depending on the command ('create' or 'update'), it calls the respective function with sorted files.
            Expects at least three arguments: the command and a list of file paths.
    """
    if len(sys.argv) < 4:
        print("Correct usage: python difupdate.py <command> <list of files> <list of files>")
        sys.exit(1)

    script_commands_list = ['update', 'create']
    if sys.argv[1] not in script_commands_list:
        print(f"Unavailable command, only available commands are: {script_commands_list}")
        sys.exit(1)

    files = []
    for arg in sys.argv[2:]:
        extension = os.path.splitext(arg)[1]
        if not extension.startswith('.'):
            print("The file extension should start with a dot")
        else:
            files.append(arg)

    files.sort()

    if sys.argv[1] == 'create':
        create_bin(files)
    if sys.argv[1] == 'update':
        update_bin(files)
