#!/usr/bin/python3
""" Module for 2d matrix rotation"""


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix 90° clockwise"""
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, down = left, right
            left_up = matrix[top][left + i]
            matrix[top][left + i] = matrix[down - i][left]
            matrix[down - i][left] = matrix[down][right - i]
            matrix[down][right - i] = matrix[top + i][right]
            matrix[top + i][right] = left_up
        right -= 1
        left += 1
