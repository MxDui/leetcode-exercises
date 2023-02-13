from typing import List
import unittest


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft

            l += 1
            r -= 1


class TestSolution(unittest.TestCase):
    def test_rotate(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

        matrix = [[5, 1, 9, 11], [2, 4, 8, 10],
                  [13, 3, 6, 7], [15, 14, 12, 16]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[15, 13, 2, 5], [14, 3, 4, 1], [
                         12, 6, 8, 9], [16, 7, 10, 11]])

        matrix = [[1]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[1]])

        matrix = [[1, 2], [3, 4]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, [[3, 1], [4, 2]])


if __name__ == '__main__':
    unittest.main()
