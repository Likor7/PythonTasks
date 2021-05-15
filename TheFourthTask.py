def fibonacci_calc(n: int):
    fibonacci = []
    i = 0
    k = 1
    for q in range(n):
        fibonacci.append(k)
        temp = k
        k += i
        i = temp
    return fibonacci


def create_matrix(element: int, amount_rows: int, amount_columns: int):
    m = []
    for i in range(amount_rows):  # A for loop for row entries
        a = []
        for j in range(amount_columns):  # A for loop for column entries
            a.append(element)
            element += 1
        m.append(a)
    return m


def print_matrix(m: list):
    print("# " * (len(m)+2))
    for i in range(len(m)):
        print('#', end='')
        for j in range(len(m[0])):
            print(m[i][j], end=" ")
        print('#')
    print("# " * (len(m) + 2))


def main():
    print(fibonacci_calc(10))

    print("\n\n\n")

    matrix = create_matrix(7, 5, 4)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
