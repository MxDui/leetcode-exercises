from typing import List
import unittest

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest,i +nums[i])
            l = r+1
            r = farthest 
            res += 1
        
        return res
    

class Test(unittest.TestCase):

    def test_jump(self):

        s = Solution()
        self.assertEqual(s.jump([2,3,1,1,4]), 2)
        self.assertEqual(s.jump([2,3,0,1,4]), 2)
        self.assertEqual(s.jump([2,3,0,1,4,1]), 3)
        self.assertEqual(s.jump([2,3,0,1,4,1,1]), 3)

if __name__ == '__main__':
    unittest.main()
        

