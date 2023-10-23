

def return_tuple_palindromes(array):
    count = 0
    maximum = -1

    for i in range(len(array)):
        value = array[i]
        copy = value
        new_number = 0
        while value:
            new_number = new_number * 10 + value % 10
            value //= 10

        if new_number == copy:
            count += 1
            if maximum < new_number:
                maximum = new_number

    return (count, maximum)

if __name__ == '__main__':
    n = int(input("Enter the number of elements our array has: "))

    print("Enter the elements separated by a space: ", end="")
    array = list(map(int, input().split()))

    count, maximum = return_tuple_palindromes(array)
    print(f"The number of palindromes is {count}, and the greatest palindrome number is {maximum}")