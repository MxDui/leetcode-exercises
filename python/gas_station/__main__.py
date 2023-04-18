from typing import List
import unittest

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i+1

        return res
        

class TestSolution(unittest.TestCase):
    def test_1(self):
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        self.assertEqual(Solution().canCompleteCircuit(gas, cost), 3)

    def test_2(self):
        gas = [2,3,4]
        cost = [3,4,3]
        self.assertEqual(Solution().canCompleteCircuit(gas, cost), -1)


if __name__ == '__main__':
    unittest.main()