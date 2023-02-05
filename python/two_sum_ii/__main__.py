from typing import List
import unittest

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]

        return []


class Test(unittest.TestCase):

    def test_twoSum(self):
        numbers = [2, 7, 11, 15]
        target = 9
        res = [1, 2]
        self.assertEqual(Solution().twoSum(numbers, target), res)

        numbers = [2, 3, 4]
        target = 6
        res = [1, 3]
        self.assertEqual(Solution().twoSum(numbers, target), res)

        numbers = [-1, 0]
        target = -1
        res = [1, 2]
        self.assertEqual(Solution().twoSum(numbers, target), res)

if __name__ == "__main__":
    unittest.main()