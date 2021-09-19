from numpy import array , zeros, dot

A = array([[5., 8., -1.],[1.,  2.,  3.], [ 2.,  -3.,  2.]])
B = array([[16.],[10.],[5.]])
for i in A:
    print(i)

# Gauss Elimination using partial pivoting

def solve_equation(A, b):
    n = len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    # k represents the current pivot row. Since GE traverses the matrix in the upper
    # right triangle, we also use k for indicating the k-th diagonal column index.
    for k in range(n-1): # k = 0, 1, 2
        # Choose largest pivot element below (and including) k
        maxindex = abs(A[k:, k]).argmax() + k
        print('maxindex ', maxindex)
        print('k ', k)
        if A[maxindex, k] == 0:
            raise ValueError("Matrix is singular.")
        # Swap rows
        if maxindex != k:
            A[[k, maxindex]] = A[[maxindex, k]]
            b[[k, maxindex]] = b[[maxindex, k]]
        for row in range(k+1, n):
            multiplier = A[row][k]/A[k][k] # ділимо кожен елемент стовпця на
            print('a[row][k] = ', A[row][k])
            # the only one in this column since the rest are zero
            A[row][k] = multiplier
            for col in range(k + 1, n):
                A[row][col] = A[row][col] - multiplier*A[k][col]
            # Equation solution column
            b[row] = b[row] - multiplier*b[k]

    x = zeros(n)
    k = n-1
    x[k] = b[k]/A[k, k]
    while k >= 0:
        x[k] = (b[k] - dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x
Aug = solve_equation(A, B)
# print(Aug)
