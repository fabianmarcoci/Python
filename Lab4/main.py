from Queue import Queue
from Stack import Stack
from Matrix import Matrix

if __name__ == '__main__':
    s = Stack()

    # Test is_empty on a new stack
    print(s.is_empty())  # Should return True

    # Push elements into the stack
    s.push('apple')
    s.push('banana')
    s.push('cherry')

    print(s.peek())

    print(s.pop())
    print(s.pop())
    print(s.pop())

    print(s.is_empty())

    q = Queue()

    print(q.is_empty())

    q.push('apple')
    q.push('banana')
    q.push('pineapple')

    print(q.peek())

    print(q.pop())
    print(q.pop())
    print(q.pop())

    print(q.is_empty())

    matrix = Matrix(2, 3)
    matrix.initialize_matrix([
        [1, 0, 3],
        [4, 5, 6]])
    matrix.print_matrix()
    matrix.set_element(0, 1, 2)
    print("---------")
    matrix.print_matrix()

    t_m = Matrix(3, 2)
    t_m.initialize_matrix(matrix.get_transposed_matrix())
    print("---------")
    t_m.print_matrix()

    c = Matrix(2, 2)
    c.initialize_matrix(t_m.multiply_matrix(matrix))
    if c:
        print("---------")
        c.print_matrix()

        c.apply_transformation(lambda x: x % 2)
        print("---------")
        c.print_matrix()