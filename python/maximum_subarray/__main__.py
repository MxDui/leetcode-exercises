from typing import List
import unittest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]

        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_2(self):
        self.assertEqual(Solution().maxSubArray([1]), 1)

    def test_3(self):
        self.assertEqual(Solution().maxSubArray([5, 4, -1, 7, 8]), 23)


if __name__ == "__main__":
    unittest.main()
