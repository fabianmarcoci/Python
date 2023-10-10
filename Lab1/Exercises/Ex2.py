


def count_vowels(word):
    counter = 0
    for char in word.lower():
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            counter = counter + 1

    return counter

if __name__ == '__main__':
    word = input("The string is: ")

    x = count_vowels(word)
    print(f"The number of vowels in {word} is: {x}")