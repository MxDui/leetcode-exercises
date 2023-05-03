from typing import List
import unittest

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i


        return True if goal == 0 else False
            

class Test(unittest.TestCase):

    def test_canJump(self):
        sol = Solution()

        # Test case 1
        self.assertEqual(sol.canJump([2,3,1,1,4]), True)

        # Test case 2
        self.assertEqual(sol.canJump([3,2,1,0,4]), False)

        # Test case 3
        self.assertEqual(sol.canJump([0]), True)


if __name__ == "__main__":
    unittest.main()