
def counter_of_words(text):
    counter = 0
    first_word = False

    for i in range(len(text)):
        if text[i].isalpha() and first_word == False:
            counter = 1
            first_word = True
            continue

        # Special cases
        if text[i - 2] == '\'' and (text[i - 1] == 'n' or text[i - 1] == 't') and text[i].isalpha():
            counter += 1
            continue
        if text[i - 1] == ' ' and text[i].isalpha():
            counter += 1
            

    return counter


if __name__ == '__main__':
    text = input("This is the text: ")

    words_count = counter_of_words(text)

    print(f"There are {words_count} words in the text.")