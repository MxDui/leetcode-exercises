import unittest


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1

        return res


class TestNumberOf1Bits(unittest.TestCase):
    def test_number_of_1_bits(self):
        self.assertEqual(Solution().hammingWeight(n=11), 3)
        self.assertEqual(Solution().hammingWeight(n=128), 1)
        self.assertEqual(Solution().hammingWeight(n=4294967293), 31)


if __name__ == '__main__':
    unittest.main()
