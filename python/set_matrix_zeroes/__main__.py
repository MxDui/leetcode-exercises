from typing import List
import unittest


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])

        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0


class Test(unittest.TestCase):

    def test_setZeroes(self):
        s = Solution()

        matrix = [[1, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]]
        s.setZeroes(matrix)
        self.assertEqual(matrix, [[1, 0, 1],
                                   [0, 0, 0],
                                   [1, 0, 1]])

        matrix = [[0, 1, 2, 0],
                  [3, 4, 5, 2],
                  [1, 3, 1, 5]]
        s.setZeroes(matrix)
        self.assertEqual(matrix, [[0, 0, 0, 0],
                                   [0, 4, 5, 0],
                                   [0, 3, 1, 0]])
        


if __name__ == "__main__":
    unittest.main()