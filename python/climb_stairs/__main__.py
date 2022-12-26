import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one


class Test(unittest.TestCase):
    def test_climbStairs(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(2), 2)
        self.assertEqual(solution.climbStairs(3), 3)
        self.assertEqual(solution.climbStairs(4), 5)
        self.assertEqual(solution.climbStairs(5), 8)
        self.assertEqual(solution.climbStairs(6), 13)


if __name__ == '__main__':
    unittest.main()
