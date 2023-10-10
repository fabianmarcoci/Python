
def count_letters_repetition(text):
    char_count = {}
    max_count = 0
    for char in text:
        if char.isalpha():
            if char not in char_count:
                char_count[char.lower()] = 1
            else:
                char_count[char.lower()] += 1
            if max_count < char_count[char.lower()]:
                max_count = char_count[char.lower()]

    most_common_letters = [char for char, count in char_count.items() if count == max_count]

    return (most_common_letters, max_count)


if __name__ == '__main__':
    text = input("This is the text: ")

    most_common_letters, repetitions = count_letters_repetition(text)

    print(f"Most common letters in the text are: {', '.join(most_common_letters)} with {repetitions} repetitions each.")