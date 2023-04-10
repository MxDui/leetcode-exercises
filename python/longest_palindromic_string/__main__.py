import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for  i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res



class TestSolution(unittest.TestCase):
    def test_longestPalindrome(self):
        self.assertEqual(Solution().longestPalindrome("babad"), "bab")
        self.assertEqual(Solution().longestPalindrome("cbbd"), "bb")
        self.assertEqual(Solution().longestPalindrome("a"), "a")
        self.assertEqual(Solution().longestPalindrome("ac"), "a")

if __name__ == '__main__':
    unittest.main()