def transpose_matrix(m):
    return list(zip(*m))


def matrix_minor(m, i, j):
    return [row[:j] + row[j+1] for row in (m[:i] + m[i+1:])]


def matrix_determinant(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    d = 0
    for c in range(len(m)):
        d += ((-1) ** c) * m[0][c] * matrix_determinant((matrix_minor(m, 0, c)))
    return d

def inverse_matrix(m):
    d = matrix_determinant(m)

    if len(m) == 2:
        return [[m[1][1]/d, -1 * m[0][1] / d],
                [-1 * m[1][0] / d, m[0][0] / d]]
    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactor_row = []
        for c in range(len(m)):
            minor = matrix_minor(m, r, c)
            cofactor_row.append(((-1) ** (r + c)) * matrix_determinant(minor))
        cofactors.append(cofactor_row)
    cofactors = transpose_matrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / d
    return cofactors
