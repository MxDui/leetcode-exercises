import unittest


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))

        return res


class Test(unittest.TestCase):
    def test_reverseBits(self):
        n = 0b00000010100101000001111010011100
        res = 0b00111001011110000010100101000000
        self.assertEqual(Solution().reverseBits(n), res)

        n = 0b11111111111111111111111111111101
        res = 0b10111111111111111111111111111111
        self.assertEqual(Solution().reverseBits(n), res)


if __name__ == "__main__":

    unittest.main()
