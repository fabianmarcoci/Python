

def order_tuples(*lists):
    maximum = 0
    for array in lists:
        if len(array) > maximum:
            maximum = len(array)
    new_list = []
    for i in range(maximum):
        index_array = []
        for array in lists:
            if len(array) > i:
                index_array.append(array[i])
            else:
                index_array.append(None)
        new_list.append(tuple(index_array))

    return new_list

if __name__ == '__main__':
    n = int(input("Number of lists: "))
    lists = []
    for _ in range(n):
        m = int(input(f"Number of elements for list {_}: "))
        print("Elements: ", end="")
        elements = list(map(str, input().split()))
        if len(elements) != m:
            print("Wrong number of elements.")
            exit(1)
        lists.append(elements)

    tuples = order_tuples(*lists)
    print(f"Our tuples are: {tuples}")
