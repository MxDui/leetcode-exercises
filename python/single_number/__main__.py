import unittest
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n

        return res


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().singleNumber([2, 2, 1]), 1)

    def test2(self):
        self.assertEqual(Solution().singleNumber([4, 1, 2, 1, 2]), 4)

    def test3(self):
        self.assertEqual(Solution().singleNumber([1]), 1)


if __name__ == "__main__":

    unittest.main()
