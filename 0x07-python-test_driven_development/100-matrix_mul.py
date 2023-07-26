#!/usr/bin/python3

"""The Module that have matrix mul fun"""


def matrix_mul(m_a, m_b):
    """the mul function
    m_a: list of int or float
    m_b: list of int or float
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(element, list)for element in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(element, list) for element in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for row in m_a for ele in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for row in m_b for ele in row):
        raise TypeError("m_b should contain only integers or floats")

    size = len(m_a[0])
    if not all(len(row) == size for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    size = len(m_b[0])
    if not all(len(row) == size for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    mul = mul_matrix(m_a, m_b)
    return mul


def reverse_matrix(matrix):
    """
    Reverse Matrix
    matrix: list of list of int or float
    return: the reverse matrix
    """
    if not matrix:
        return None
    cols = len(matrix)
    rows = len(matrix[0])

    new_matrix = [[0 for row in range(cols)] for col in range(rows)]
    for row in range(rows):
        for col in range(cols):
            new_matrix[row][col] = matrix[col][row]
    return new_matrix


def mul_two_rows(l_a, l_b):
    """multiple to rows for mulitple two matrix"""
    re = 0
    for n in range(len(l_a)):
        re += l_a[n] * l_b[n]
    return re


def mul_matrix(m_a, m_b):
    """
    Multiplicate two matrix
    m_a: list of list of int or float
    m_b: list of list of int or float
    Return: the mul matrix
    """
    if not m_a or not m_b:
        return None
    rows = len(m_a)
    cols = len(m_b[0])
    m_b = reverse_matrix(m_b)

    mul = [[0 for row in range(cols)] for col in range(rows)]
    for row in range(rows):
        for col in range(cols):
            mul[row][col] = mul_two_rows(m_a[row], m_b[col])

    return mul
