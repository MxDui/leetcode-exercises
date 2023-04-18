from typing import List
import unittest

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMin, curMax = 1,1

        for n in nums:
            if n == 0:
                curMin,curMax = 1,1
                continue

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin,n)
            curMin = min(tmp, n * curMin,n)

            res = max(res,curMax)

        return res



class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().maxProduct([2,3,-2,4]),6)

    def test2(self):
        self.assertEqual(Solution().maxProduct([-2,0,-1]),0)

    def test3(self):
        self.assertEqual(Solution().maxProduct([2,-5,-2,-4,3]),24)

    def test4(self):
        self.assertEqual(Solution().maxProduct([-2]),-2)

    def test5(self):
        self.assertEqual(Solution().maxProduct([-2,3,-4]),24)

    def test6(self):
        self.assertEqual(Solution().maxProduct([0,2]),2)

    def test7(self):
        self.assertEqual(Solution().maxProduct([3,-1,4]),4)

    def test8(self):
        self.assertEqual(Solution().maxProduct([-1,-2,-9,-6]),108)

    def test9(self):
        self.assertEqual(Solution().maxProduct([2,3,-2,4]),6)

    def test10(self):
        self.assertEqual(Solution().maxProduct([-2,3,-4]),24)

    def test11(self):
        self.assertEqual(Solution().maxProduct([-2,0,-1]),0)

    def test12(self):
        self.assertEqual(Solution().maxProduct([2,-5,-2,-4,3]),24)

    def test13(self):
        self.assertEqual(Solution().maxProduct([0,2]),2)

    def test14(self):
        self.assertEqual(Solution().maxProduct([3,-1,4]),4)

    def test15(self):
        self.assertEqual(Solution().maxProduct([-1,-2,-9,-6]),108)

    def test16(self):
        self.assertEqual(Solution().maxProduct([-2,3,-4]),24)

    def test17(self):
        self.assertEqual(Solution().maxProduct([2,3,-2,4]),6)

    def test18(self):
        self.assertEqual(Solution().maxProduct([-2,0,-1]),0)

    def test19(self):
        self.assertEqual(Solution().maxProduct([2,-5,-2,-4,3]),24)

    def test20(self):
        self.assertEqual(Solution().maxProduct([0,2]),2)

    def test21(self):
        self.assertEqual(Solution().maxProduct([3,-1,4]),4)



if __name__ == '__main__':
    unittest.main()