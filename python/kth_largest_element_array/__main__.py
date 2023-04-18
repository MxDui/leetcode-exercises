from typing import List
import unittest


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)


class Test(unittest.TestCase):

    def test_findKthLargest(self):
        solution = Solution()
        self.assertEqual(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)


if __name__ == '__main__':
    unittest.main()