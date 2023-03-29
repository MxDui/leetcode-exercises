import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        l = 0
        res=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res, r - l +1)

        return res


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(Solution().lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring(""), 0)

if __name__ == '__main__':
    unittest.main()