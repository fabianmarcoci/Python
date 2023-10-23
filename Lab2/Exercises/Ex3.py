

def other_way(first_list, second_list):
    set_a = set(first_list)
    set_b = set(second_list)

    intersection = list(set_a & set_b)
    union = list(set_a | set_b)
    a_not_b = list(set_a - set_b)
    b_not_a = list(set_b - set_a)

    return intersection, union, a_not_b, b_not_a
def multiple_operations_on_2lists(first_list, second_list):
    intersection = []
    union = []
    a_not_b = []
    b_not_a = []
    for i in range(0, len(first_list)):
        union.append(first_list[i])
        flag = 0
        for j in range(0, len(second_list)):
            if first_list[i] == second_list[j]:
                intersection.append(first_list[i])
                flag = 1
                break
        if flag == 0:
            a_not_b.append(first_list[i])

    for j in range(0, len(second_list)):
        union.append(second_list[j])
        flag = 0
        for i in range(0, len(intersection)):
            if second_list[j] == intersection[i]:
                flag = 1
                break
        if flag == 0:
            b_not_a.append(second_list[j])


    return intersection, union, a_not_b, b_not_a


if __name__ == '__main__':
    n = int(input("First list size: "))
    m = int(input("Second list size: "))
    first_list = [int(input("Enter element {} of the first list: ".format(i + 1))) for i in range(n)]
    second_list = [int(input("Enter element {} of the second list: ".format(i + 1))) for i in range(n)]

    intersection, union, a_not_b, b_not_a = multiple_operations_on_2lists(first_list, second_list)

    print(f"The union of the 2 lists is: {union}")
    print(f"The intersection of the 2 lists is: {intersection}")
    print(f"The elements present in first list that don't exist in the second list: {a_not_b}")
    print(f"The elements present in second list that don't exist in the first list: {b_not_a}")