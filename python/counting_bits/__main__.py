import unittest
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp
    
class TestSolution(unittest.TestCase):
    def test_countBits(self):
        self.assertEqual(Solution().countBits(2), [0,1,1])
        self.assertEqual(Solution().countBits(5), [0,1,1,2,1,2])

if __name__ == '__main__':
    unittest.main()