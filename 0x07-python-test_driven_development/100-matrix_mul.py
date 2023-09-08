#!/usr/bin/python3
"""
Module of multiply two matrix
"""


def matrix_mul(m_a, m_b):
    """
    this function is going to multiply two matrix
    argument:
             m_a: the first matrix
             m_b: the second matrix
    return: the matrix result or Raises an error
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    width = len(m_a[0])
    for i in m_a:
        if len(i) != width:
            raise TypeError("each row of m_a must be of the same size")
    width = len(m_b[0])
    for i in m_b:
        if len(i) != width:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for x, y in zip(m_a, m_b):
        for i, j in zip(x, y):
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    result_matrix = []
    for i in range(len(m_a)):
        line_element = []
        for j in range(width):
            element = 0
            for k in range(width):
                element += m_a[i][k] * m_b[k][j]
            line_element.append(element)
        result_matrix.append(line_element)
    return result_matrix


if __name__ == "__main__":
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
