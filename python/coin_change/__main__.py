from typing import List
import unittest

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a],1+dp[a-c])

        return dp[amount] if dp[amount] != amount + 1 else -1
    

class Test(unittest.TestCase):
    def test_coinChange(self):
        s = Solution()

        self.assertEqual(s.coinChange([1, 2, 5], 11), 3)
        self.assertEqual(s.coinChange([2], 3), -1)
        self.assertEqual(s.coinChange([1], 0), 0)
        self.assertEqual(s.coinChange([1], 1), 1)
        self.assertEqual(s.coinChange([1], 2), 2)


if __name__ == "__main__":
    unittest.main()