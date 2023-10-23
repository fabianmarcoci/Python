

def field_vision(matrix):
    positions = []

    for j in range(len(matrix[0])):
        max = 0
        for i in range(len(matrix)):
            if matrix[i][j] <= max:
                positions.append((i, j))
            if max < matrix[i][j]:
                max = matrix[i][j]

    return positions

if __name__ == '__main__':
    rows = int(input("Insert the number of rows: "))
    cols = int(input("Insert the number of rows: "))

    print("Enter elements separated by space, each row by enter: ")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))

        if len(row) != cols:
            print("Incorrect number of elements.")
            exit(1)

        matrix.append(row)

    array = field_vision(matrix)
    print(f"The persons who have no vision on the field are: {array}")

