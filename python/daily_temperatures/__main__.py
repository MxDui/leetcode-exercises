from typing import List
import unittest

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT,stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_dailyTemperatures(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        self.assertEqual(self.sol.dailyTemperatures(temperatures), [1, 1, 4, 2, 1, 1, 0, 0])

if __name__ == "__main__":
    unittest.main()