#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """This function prints a matrix of integer

    Arg:

    matrix: parameter list of list of integers
    """
    for elements in matrix:
        for element in range(0, len(elements)):
            print("{:d}".format(elements[element]), end=" " if elements[element] != elements[-1] else "")
        print()
