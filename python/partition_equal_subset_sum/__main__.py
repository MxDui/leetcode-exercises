from typing import List
import unittest

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
    
        dp = set()

        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for t in dp:
                if (t+nums[i]) == target:
                    return True
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp = nextDP

        return True if target in dp else False
    

class Test(unittest.TestCase):
    def test_canPartition(self):
        s = Solution()
        self.assertEqual(s.canPartition([1,5,11,5]), True)
        self.assertEqual(s.canPartition([1,2,3,5]), False)
        self.assertEqual(s.canPartition([1,2,5]), False)
        self.assertEqual(s.canPartition([1,2,3,4,5,6,7]), True)
        self.assertEqual(s.canPartition([1,2,3,4,5,6,7,8]), True)

if __name__ == '__main__':
    unittest.main()