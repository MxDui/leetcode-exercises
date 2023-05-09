import unittest


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "12"
        self.assertEqual(Solution().numDecodings(s), 2)

    def test_2(self):
        s = "226"
        self.assertEqual(Solution().numDecodings(s), 3)


if __name__ == "__main__":
    unittest.main()
