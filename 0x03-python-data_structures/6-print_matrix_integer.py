#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """This function prints a matrix of integer

    Arg:

    matrix: parameter list of list of integers
    """
    for elements in matrix:
        for element in range(0, len(elements)):
            if element != len(elements) - 1:
                print("{}".format(elements[element]), end=" ")
            else:
                print("{}".format(elements[element]))
