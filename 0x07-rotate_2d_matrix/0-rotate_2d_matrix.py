#!/usr/bin/python3
"""
Given an n x n 2D matrix,
rotate it 90 degrees clockwise
"""


# def rotate_2d_matrix(matrix):
#     n = len(matrix)

#     for i in range(n):
#         for j in range(i, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#         for i in range(len(matrix)):
#             matrix[i] = matrix[i][::-1]

def rotate_2d_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
        
