from typing import List
import unittest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height) -1

        while l < r:
            area = (r - l) * min(height[l],height[r])
            res = max(res,area)

            if height[l] < height[r]:
                l +=1
            else:
                r -=1
        
        return res


class TestSolution(unittest.TestCase):
    def test_maxArea(self):
        self.assertEqual(Solution().maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(Solution().maxArea([1,1]), 1)
        self.assertEqual(Solution().maxArea([4,3,2,1,4]), 16)
        self.assertEqual(Solution().maxArea([1,2,1]), 2)


if __name__ == '__main__':
    unittest.main()