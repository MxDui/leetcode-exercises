from typing import List
import unittest


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i+1, subset)
        backtrack(0, [])

        return res


class TestSolution(unittest.TestCase):
    def test_subsetsWithDup(self):
        self.assertEqual(sorted(Solution().subsetsWithDup([1, 2, 2])), sorted(
            [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]))

        self.assertEqual(sorted(Solution().subsetsWithDup([0])), sorted(
            [[], [0]]))

        self.assertEqual(sorted(Solution().subsetsWithDup([1, 2, 3])), sorted(
            [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]))


if __name__ == '__main__':
    unittest.main()
