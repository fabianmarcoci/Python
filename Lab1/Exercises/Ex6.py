

def palindrome_check(n):
    reversed_number = 0
    copy = n
    while(copy):
        reversed_number = reversed_number * 10 + copy % 10
        copy //= 10

    if (reversed_number == n):
        return True

    return False

if __name__ == '__main__':
    n = int(input("The given number is: "))

    is_palindrome = palindrome_check(n)

    if(is_palindrome == True):
        print(f"This number {n} is a palindrome.")
    else:
        print(f"This number {n} isn't a palindrome.")
