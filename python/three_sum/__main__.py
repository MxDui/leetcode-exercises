from typing import List
import unittest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


class Test(unittest.TestCase):
    def test_threeSum(self):
        solution = Solution()
        self.assertEqual(
            solution.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]
        )
        self.assertEqual(solution.threeSum([]), [])
        self.assertEqual(solution.threeSum([0]), [])
        self.assertEqual(solution.threeSum([0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(solution.threeSum([-2, 0, 1, 1, 2]), [[-2, 0, 2], [-2, 1, 1]])
        self.assertEqual(solution.threeSum([1, 2, -2, -1]), [])


if __name__ == "__main__":
    unittest.main()
