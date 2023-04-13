from typing import List
import unittest

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} #(index,total) -> # of ways
        def backtrack(i,total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)] = (backtrack(i+1,total+nums[i]) +
                            backtrack(i+1,total-nums[i]))

            return dp[(i,total)]


        return backtrack(0,0)


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findTargetSumWays([1,1,1,1,1],3),5)

    def test2(self):
        self.assertEqual(Solution().findTargetSumWays([1],1),1)

    def test3(self):
        self.assertEqual(Solution().findTargetSumWays([1],2),0)

    def test4(self):
        self.assertEqual(Solution().findTargetSumWays([1,0],1),2) 



if __name__ == '__main__':
    unittest.main()