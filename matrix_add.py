"""
Write a function named matrix_add that accepts a pair of two-dimensional lists of integers as parameters,
treats the lists as 2D matrices and adds them, returning the result. The sum of two matrices A and B is a matrix C where for every row i and column j, Cij = Aij + Bij.
You may assume that the lists passed as parameters have the same dimensions.
"""
def matrix_add(a,b):
    c = a.copy()
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]


    return c
