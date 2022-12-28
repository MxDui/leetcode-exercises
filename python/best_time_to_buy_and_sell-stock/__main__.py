import unittest
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # left for buy and right for sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]

                maxP = max(maxP, profit)

            else:
                l = r

            r = r+1
        return maxP



class Test(unittest.TestCase):
    def test_maxProfit(self):
        prices = [7, 1, 5, 3, 6, 4]
        maxP = 5
        self.assertEqual(Solution().maxProfit(prices), maxP)

        prices = [7, 6, 4, 3, 1]
        maxP = 0
        self.assertEqual(Solution().maxProfit(prices), maxP)

        prices = [2, 4, 1]
        maxP = 2
        self.assertEqual(Solution().maxProfit(prices), maxP)

        prices = [2, 1, 2, 1, 0, 1, 2]
        maxP = 2
        self.assertEqual(Solution().maxProfit(prices), maxP)


if __name__ == "__main__":
    unittest.main()