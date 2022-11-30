import unittest

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1


        while l <= r:
            m = ((l+r) // 2)

            if nums[m] > target:
                r = m - 1 
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
        

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(Solution().search(nums=[-1,0,3,5,9,12], target=9), 4)
        self.assertEqual(Solution().search(nums=[-1,0,3,5,9,12], target=2), -1)
        self.assertEqual(Solution().search(nums=[5], target=5), 0)

if __name__ == '__main__':
    unittest.main()