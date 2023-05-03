import unittest


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                res += 1
                l -= 1
                r += 1

            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[r] == s[l]:
                res += 1
                l -= 1
                r += 1

        return res


class Test(unittest.TestCase):
    def test_countSubstrings(self):
        s = Solution()

        self.assertEqual(s.countSubstrings("abc"), 3)
        self.assertEqual(s.countSubstrings("aaa"), 6)
        self.assertEqual(s.countSubstrings("abba"), 6)
        self.assertEqual(s.countSubstrings("abccba"), 9)
        self.assertEqual(s.countSubstrings("abccda"), 7)


if __name__ == "__main__":
    unittest.main()
