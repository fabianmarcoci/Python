

def extract_number(text):
    flag = False
    n = 0
    for char in text:
        if (char >= '0' and char <= '9'):
            flag = True
            n = n * 10 + int(char) - int('0')
            continue
        if (flag == True):
            break

    return n

if __name__ == '__main__':
    text = input("The text is: ")
    n = extract_number(text)

    print(f"The number extracted from the text is: {n}")