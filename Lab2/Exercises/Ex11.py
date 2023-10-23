

def order_list_of_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1][2])

if __name__ =='__main__':
    n = int(input("Number of tuples: "))
    lists = []
    print("Tuples: ", end="")
    for _ in range(n):
        tuple_input = tuple(input().split(', '))
        lists.append(tuple_input)

    ordered_lists = order_list_of_tuples(lists)
    print(f"Our ordered tuples are: {ordered_lists}")
