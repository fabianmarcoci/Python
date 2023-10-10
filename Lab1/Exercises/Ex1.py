

def greatest_common_divisor(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        while num:
            temp = result
            result = num
            num = temp % num

    return result


if __name__ == '__main__':
    n = int(input("Number of numbers: "))
    numbers = [0] * n

    for i in range(n):
        numbers[i] = int(input(f"Number {i + 1}: "))


    x = greatest_common_divisor(numbers)
    print(f"Greatest common divisor is: {x}")
