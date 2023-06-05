from typing import List
import unittest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(s.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(s.search([1], 0), -1)
        self.assertEqual(s.search([1], 1), 0)
        self.assertEqual(s.search([1, 3], 3), 1)
        self.assertEqual(s.search([3, 1], 1), 1)
        self.assertEqual(s.search([3, 1], 3), 0)
        self.assertEqual(s.search([3, 5, 1], 3), 0)


if __name__ == "__main__":
    unittest.main()
