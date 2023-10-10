
def check(matrix, next_x, next_y):
    if (next_x < 0 or next_x >= len(matrix) or
            next_y < 0 or next_y >= len(matrix[0]) or
            matrix[next_x][next_y] == '^'):
        return 1

    return 0
def unspiral(matrix):
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x = 0
    y = 0
    chars = []
    same_dir = [0, 1]
    while True:
        chars.append(matrix[x][y])
        matrix[x][y] = '^'
        j = 0
        while j < 4:
            # Extra check to keep the direction
            if (check(matrix, x + same_dir[0], y + same_dir[1]) == 0):
                x = x + same_dir[0]
                y = y + same_dir[1]
                break

            next_x = x + dir[j][0]
            next_y = y + dir[j][1]
            same_dir[0] = dir[j][0]
            same_dir[1] = dir[j][1]
            if (check(matrix, next_x, next_y) == 1):
                j += 1
            else:
                x = next_x
                y = next_y
                break

        if j == 4:
            break
    return chars


if __name__ == '__main__':
    rows = int(input("Number of rows in the matrix: "))
    cols = int(input("Number of columns in the matrix: "))

    matrix = []
    for r in range(rows):
        row = list(input(f"Enter row {r + 1} (without spaces): "))
        matrix.append(row)

    spiral_string = unspiral(matrix)

    print(f"The string is: {''.join(spiral_string)}")
