from typing import List
import unittest

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]

        one, i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0

            else:
                digits.append(1)
                one = 0
            i += 1

        return digits[::-1]


class TestSolution(unittest.TestCase):
    def test_plus_one(self):
        self.assertEqual(Solution().plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(Solution().plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(Solution().plusOne([0]), [1])
        self.assertEqual(Solution().plusOne([9]), [1, 0])
        self.assertEqual(Solution().plusOne([9, 9]), [1, 0, 0])
        self.assertEqual(Solution().plusOne([9, 9, 9]), [1, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()