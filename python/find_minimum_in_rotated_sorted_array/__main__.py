from typing import List
import unittest

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r= 0,len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break

            m = (l+r) // 2
            res = min(res,nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
            
        return res
    

class Test(unittest.TestCase):

    def test(self):
        s = Solution()

        self.assertEqual(s.findMin([3,4,5,1,2]),1)
        self.assertEqual(s.findMin([4,5,6,7,0,1,2]),0)
        self.assertEqual(s.findMin([11,13,15,17]),11)
        self.assertEqual(s.findMin([2,1]),1)
        self.assertEqual(s.findMin([1,2]),1)


if __name__ == '__main__':
    unittest.main()