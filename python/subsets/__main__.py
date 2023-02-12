from typing import List
import unittest

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # add nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # don't add nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)

        return res


class TestSolution(unittest.TestCase):
    def test_subsets(self):
        self.assertEqual(sorted(Solution().subsets([1, 2, 3])), sorted([[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]))
        self.assertEqual(sorted(Solution().subsets([0])), sorted([[0], []]))
        self.assertEqual(sorted(Solution().subsets([])), sorted([[]]))

if __name__ == '__main__':
    unittest.main()