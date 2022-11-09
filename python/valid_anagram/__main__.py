import unittest
from typing import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)


class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(Solution().isAnagram("anagram", "nagaram"))
        self.assertFalse(Solution().isAnagram("rat", "car"))

if __name__ == '__main__':
    unittest.main()