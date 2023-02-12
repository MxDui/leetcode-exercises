import unittest


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = helper(x, n // 2)
            res = res * res
            return x * res if n % 2 else res

        res = helper(x, abs(n))

        return res if n >= 0 else 1 / res


class TestSolution(unittest.TestCase):
    def test_my_pow(self):
        self.assertEqual(Solution().myPow(2.00000, 10), 1024.00000)
        self.assertEqual(Solution().myPow(2.10000, 3), 9.261000000000001)
        self.assertEqual(Solution().myPow(2.00000, -2), 0.25000)


if __name__ == '__main__':
    unittest.main()
