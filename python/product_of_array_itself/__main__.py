from typing import List
import unittest

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        res = [1] * (len(nums))

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1 
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix

            postfix *= nums[i]

        return res 
    
class Test(unittest.TestCase):

    def test_productExceptSelf(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(s.productExceptSelf([1,2,3,4,5]), [120,60,40,30,24])
        self.assertEqual(s.productExceptSelf([1,2,3,4,5,6]), [720,360,240,180,144,120])
        self.assertEqual(s.productExceptSelf([1,2,3,4,5,6,7]), [5040,2520,1680,1260,1008,840,720])
        self.assertEqual(s.productExceptSelf([1,2,3,4,5,6,7,8]), [40320,20160,13440,10080,8064,6720,5760,5040])

if __name__ == '__main__':
    unittest.main()