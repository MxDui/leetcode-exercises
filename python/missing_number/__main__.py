import unittest
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])

        return res


class TestSolution(unittest.TestCase):
    def test_missingNumber(self):
        solution = Solution()
        self.assertEqual(solution.missingNumber([3,0,1]),2)
        self.assertEqual(solution.missingNumber([0,1]),2)
        self.assertEqual(solution.missingNumber([9,6,4,2,3,5,7,0,1]),8)
        self.assertEqual(solution.missingNumber([0]),1)

if __name__ == '__main__':
    unittest.main()