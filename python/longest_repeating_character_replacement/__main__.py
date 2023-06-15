import unittest
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
    
class UnitTest(unittest.TestCase):

    def test_case_1(self):
        s = "ABAB"
        k = 2
        self.assertEqual(Solution().characterReplacement(s, k), 4)

    def test_case_2(self):
        s = "AABABBA"
        k = 1
        self.assertEqual(Solution().characterReplacement(s, k), 4)

    def test_case_3(self):
        s = "ABAA"
        k = 0
        self.assertEqual(Solution().characterReplacement(s, k), 2)

    def test_case_4(self):
        s = "A"
        k = 0
        self.assertEqual(Solution().characterReplacement(s, k), 1)


if __name__ == '__main__':
    unittest.main()