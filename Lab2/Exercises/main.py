

def ex1():
    n = int(input("Enter how many fibonacci numbers you want to have in your list: "))
    a = 0
    b = 1
    my_list = [a, b]

    while n:
        c = a + b
        a = b
        b = c
        my_list.append(c)
        n -= 1
    print(f"Your fibonacci sequence looks like this: {my_list}")

def is_prime_ex2(element):
    if element < 2:
        return False
    for i in range(2, int(element**0.5) + 1):
        if element % i == 0:
            return False
    return True
def ex2():
    prime_list = []
    n = int(input("Size of your list: "))
    my_list = [int(input("Enter element {}: ".format(i + 1))) for i in range(n)]

    for element in my_list:
        if is_prime_ex2(element):
            prime_list.append(element)

    print(f"Prime numbers from the list are: {prime_list}")




if __name__ == '__main__':
    ex1()
    ex2()