from typing import List
import math
import unittest

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        res = r

        while l <= r:
            k = (l + r )//2
            hours = 0
            for p in piles:
                hours += math.ceil((p / k))

            if hours <= h:
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1


        return res


class Test(unittest.TestCase):
    def test(self):
        piles = [3,6,7,11]
        h = 8
        out = 4
        self.assertEqual(Solution().minEatingSpeed(piles,h),out)
        piles = [30,11,23,4,20]
        h = 5
        out = 30
        self.assertEqual(Solution().minEatingSpeed(piles,h),out)
        piles = [30,11,23,4,20]
        h = 6
        out = 23
        self.assertEqual(Solution().minEatingSpeed(piles,h),out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
