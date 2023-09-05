#!/usr/bin/python3
"""
Divided all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    this function used to divid matrix
    """
    str_err = "matrix must be a matrix (list of lists) of integers/floats"
    divided_matrix = []
    if type(div) in [int, float]:
        if div == 0:
            raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
    if len(matrix) == 0:
        return []
    row_len = len(matrix[0])
    for i in matrix:
        line = []
        if row_len != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) in [int, float]:
                j = round(j / div, 2)
                line.append(j)
            else:
                raise TypeError(str_err)
        divided_matrix.append(line)
    return divided_matrix

if __name__ == "__main__":
    #import doctest
    #doctest.testfile("./tests/2-matrix_divided.txt")
    print(matrix_divided([[1, 3], [2]], 1)) 
