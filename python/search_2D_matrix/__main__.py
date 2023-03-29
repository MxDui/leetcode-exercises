from typing import List
import unittest

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])

        top,bottom = 0, rows-1

        while top<= bottom:
            row = (top+bottom) //2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not (top<=bottom):
            return False

        row = (top+bottom) //2
        l,r = 0,cols -1
        while l<=r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m -1
            else:
                return True
            
        return False


class TestSolution(unittest.TestCase):
    def test_searchMatrix(self):
        self.assertEqual(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), True)
        self.assertEqual(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), False)

if __name__ == '__main__':
    unittest.main()