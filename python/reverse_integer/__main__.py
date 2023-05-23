import unittest
import math

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0 

        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res


class Test(unittest.TestCase):
    def test(self):
        x = 123
        out = 321
        self.assertEqual(Solution().reverse(x),out)
        x = -123
        out = -321
        self.assertEqual(Solution().reverse(x),out)
        x = 120
        out = 21
        self.assertEqual(Solution().reverse(x),out)
        x = 0
        out = 0
        self.assertEqual(Solution().reverse(x),out)
        x = 1534236469
        out = 0
        self.assertEqual(Solution().reverse(x),out)
        x = -2147483648
        out = 0
        self.assertEqual(Solution().reverse(x),out)
        x = 2147483647
        out = 0
        self.assertEqual(Solution().reverse(x),out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)