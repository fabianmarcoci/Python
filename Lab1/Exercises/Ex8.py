

def count_the_1bits(n):
    counter = 0

    while(n):
        if (n % 2 == 1):
            counter += 1
        n //= 2

    return counter

if __name__ == '__main__':
    n = int(input("The number is: "))

    bits_count = count_the_1bits(n)

    print(f"The number of bits with value 1 {n} has is: {bits_count}")