from typing import List
import unittest

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)

        while left < right and top < bottom:
            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top,bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not(left<right and top < bottom):
                break

            for i in range(right-1, left-1,-1):
                res.append(matrix[bottom - 1][i])
            
            bottom -= 1

            for i in range(bottom - 1,top -1,-1):
                res.append(matrix[i][left])
            
            left += 1
        
        return res


class Test(unittest.TestCase):
    def test(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        out = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(Solution().spiralOrder(matrix),out)
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        out = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(Solution().spiralOrder(matrix),out)
        matrix = [[1,2,3,4]]
        out = [1,2,3,4]
        self.assertEqual(Solution().spiralOrder(matrix),out)
       

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)