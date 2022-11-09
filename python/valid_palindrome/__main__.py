import unittest


# A phrase is a palindrome if, after converting all uppercase letters into lowercase
# letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward.
#  Alphanumeric characters include letters and numbers.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        if (s == " "):
            return True

        p = ''.join(filter(str.isalnum,s.lower()))

        return p == p[::-1]






class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(Solution().isPalindrome(s="A man, a plan, a canal: Panama"))
        self.assertFalse(Solution().isPalindrome(s="race a car"))
        self.assertTrue(Solution().isPalindrome(s=" "))

if __name__ == '__main__':
    unittest.main()