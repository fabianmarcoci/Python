


def count_occurrences(firstString, secondString):
    if len(firstString) > len(secondString):
        return 0

    counter = 0
    indexOfFirst = 0
    iRetake = 0
    i = 0
    while i < len(secondString):
        if firstString[indexOfFirst] == secondString[i]:
            if indexOfFirst == len(firstString) - 1:
                counter = counter + 1
                indexOfFirst = 0
                i = iRetake + 1
                continue
            else:
                indexOfFirst = indexOfFirst + 1
                if indexOfFirst == 1:
                    iRetake = i
        else:
            cpy = indexOfFirst
            indexOfFirst = 0
            if cpy != 0:
                i = iRetake + 1
                continue
        i = i + 1

    return counter


if __name__ == '__main__':
    firstString = input("First string: ")
    secondString = input("Second string: ")

    x = count_occurrences(firstString, secondString)
    print(f"Number of occurrences of the first string in the second is: {x}")