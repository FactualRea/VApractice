# Write a function `make_matrix(m, n, value)` that returns a 2D list of m rows and n columns
# filled with `value`.


def make_matrix(m, n, value):
    matrix = []
    for i in range(m):
        row = []
        matrix.append(row)
        for j in range(n):
            row.append(value)
    return matrix

print(make_matrix(3, 5, None))
print(make_matrix(4, 2, "x"))
print(make_matrix(2, 2, 0))