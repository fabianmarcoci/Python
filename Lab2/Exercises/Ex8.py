
def ASCII_divisibility(x=1, lists=[], flag=True):
    new_list = []
    if flag == True:
        for element in lists:
            new_el = []
            for character in element:
                if ord(character) % x == 0:
                    new_el.append(character)
            new_list.append(''.join(new_el))
    else:
        for element in lists:
            new_el = []
            for character in element:
                if ord(character) % x != 0:
                    new_el.append(character)
            new_list.append(''.join(new_el))
    return new_list

if __name__ == '__main__':
    n = int(input("Number of elements: "))
    print("Elements: ", end="")
    array = list(map(str, input().split()))

    x = int(input("Number elements should be divided to: "))

    flag_input = input("Flag (True/False): ")
    flag = flag_input.lower() == "true"

    new_array = ASCII_divisibility(x, array, flag)
    print(f"The new array is: {new_array}")
