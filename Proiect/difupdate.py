import sys
import os


def check_file(file_name):
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


def create_file(file_name):
    return check_file(file_name)


def try_open_file_read_bin(file_path):
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
    if arg_files[0] != 'abc.latest':
        print('Script command should contain abc.latest file')
        sys.exit(1)

    file_path = 'abc.diff.bak'
    diff_file = create_file(file_path)

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
    if arg_files[0] != 'abc.diff':
        print('Script command should contain abc.diff file')
        sys.exit(1)

    file_path = 'abc.latest.bak'
    latest_file = create_file(file_path)
    check_file(latest_file)

    try:
        with open(latest_file, 'wb') as file:
            for i in range(1, len(arg_files)):
                complete_version = apply_commands(arg_files[i], arg_files[0])
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
