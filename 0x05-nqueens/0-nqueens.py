#!/usr/bin/python3
"""completes the nqueens challenge"""

import sys


def nQueens(N):
    """ nqueen function"""
    column = set()
    plus = set()
    minus = set()

    board = []

    def backtrack(rows):
        """displays the backtrack method"""
        if rows == N:
            print(board)
            return

        for c in range(N):
            if c in column or (rows + c) in plus \
                    or (rows - c) in minus:
                continue

            column.add(c)
            plus.add(rows + c)
            minus.add(rows - c)
            board.append([rows, c])

            backtrack(rows + 1)

            column.remove(c)
            plus.remove(rows + c)
            minus.remove(rows - c)
            board.remove([rows, c])

    backtrack(0)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)
nQueens(int(sys.argv[1]))
