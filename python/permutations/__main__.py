from typing import List
import unittest

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        if (len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):

            n = nums.pop(0)

            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)

        return res


class TestSolution(unittest.TestCase):
    def test_permute(self):
        self.assertEqual(sorted(Solution().permute([1, 2, 3])), sorted(
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]))
        self.assertEqual(sorted(Solution().permute([0, 1])), sorted(
            [[0, 1], [1, 0]]))
        self.assertEqual(sorted(Solution().permute([1])), sorted([[1]]))

if __name__ == '__main__':
    unittest.main()