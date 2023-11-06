class Matrix:

    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]

    def initialize_matrix(self, matrix):
        if len(matrix) != self.rows or any(len(row) != self.cols for row in matrix):
            print("Invalid matrix size.")
            return False
        self.matrix = matrix
        return True

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def set_element(self, i, j, value):
        if i >= self.rows or j >= self.cols:
            print("Index out of range.")
            return False
        self.matrix[i][j] = value
        return True

    def get_element(self, i, j):
        if i >= self.rows or j >= self.cols:
            print("Index out of range.")
            return None
        return self.matrix[i][j]

    def get_transposed_matrix(self):
        transposed_matrix = []

        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(self.matrix[j][i])

            transposed_matrix.append(row)

        return transposed_matrix

    def multiply_matrix(self, other):
        if self.cols != other.rows:
            print("Columns number of first matrix must be equal to rows number of second.")
            return False

        result = []

        for i in range(other.rows):
            row = []
            for j in range(self.cols):
                c = 0
                for ij in range(self.rows):
                    a = other.get_element(i, ij) * self.matrix[ij][j]
                    c += a
                row.append(c)
            result.append(row)

        return result

    def apply_transformation(self, transform):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = transform(self.matrix[i][j])