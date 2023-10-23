

def remove_under_main_diagonal(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
            else:
                break

    return matrix


if __name__ == '__main__':
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    print("Enter the matrix (each row on a new line, values separated by spaces): ")

    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != columns:
            print("Incorrect number of values entered.")
            exit(1)
        matrix.append(row)


    new_matrix = remove_under_main_diagonal(matrix)

    print("The new matrix is:")
    for row in new_matrix:
        print(row)