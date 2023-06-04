from typing import List
import unittest

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    

class Test(unittest.TestCase):
    def test_longestConsecutive(self):
        s = Solution()
        self.assertEqual(s.longestConsecutive([100,4,200,1,3,2]), 4)
        self.assertEqual(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]), 9)
        self.assertEqual(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1,9]), 10)

if __name__ == '__main__':
    unittest.main()