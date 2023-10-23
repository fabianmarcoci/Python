def find_common_elements(lists, x):
    freq = {}

    for lst in lists:
        for item in lst:
            freq[item] = freq.get(item, 0) + 1

    return [key for key, value in freq.items() if value == x]

if __name__ == '__main__':
    n = int(input("Enter the number of lists: "))
    lists = []
    print("Enter the elements each element separated by space, each list on another line: ")
    while n:
        array = list(map(str, input().split()))
        lists.append(array)
        n -= 1

    no_repetitions = int(input("Enter the number of repetition you're looking for: "))
    common_list = find_common_elements(lists, no_repetitions)
    print(f"The list of elements repeated {no_repetitions} times are: {common_list}")