
def convert_into_underscorecase(word):
    chars = list(word)
    i = 1
    if(chars[0].isupper()):
        chars[0] = chars[0].lower()

    while i < len(chars):
        if chars[i].isupper():
            chars[i] = chars[i].lower()
            chars.insert(i, '_')
            i += 1
        i += 1
    return ''.join(chars)



if __name__ == '__main__':
    word = input("The string is: ")
    chars = convert_into_underscorecase(word)

    print(f"The word in lowercase_with_underscores looks like this: {chars}")