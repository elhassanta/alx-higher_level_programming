#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """This function prints a matrix of integer

    Arg:

    matrix: parameter list of list of integers
    """
    for lin in matrix:
        for i in range(0, len(lin)):
            print("{:d}".format(lin[i]), end=" " if lin[i] != lin[-1] else "")
        print()
