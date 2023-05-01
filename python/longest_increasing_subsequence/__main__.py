from typing import List
import unittest


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


class Test(unittest.TestCase):
    def test_lengthOfLIS(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(Solution().lengthOfLIS(nums), 4)
        nums = [0, 1, 0, 3, 2, 3]
        self.assertEqual(Solution().lengthOfLIS(nums), 4)
        nums = [7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(Solution().lengthOfLIS(nums), 1)


if __name__ == "__main__":
    unittest.main()
