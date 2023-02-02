from typing import List
import unittest
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0,0

        while True:



            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow2


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(Solution().findDuplicate([1,3,4,2,2]),2)
        self.assertEqual(Solution().findDuplicate([3,1,3,4,2]),3)
        self.assertEqual(Solution().findDuplicate([1,1]),1)
        self.assertEqual(Solution().findDuplicate([1,1,2]),1)

if __name__ == '__main__':
    unittest.main()
    