from typing import List
import unittest

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0

        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end,prevEnd)

            
        return res


class TestSolution(unittest.TestCase):

    def test_eraseOverlapIntervals(self):
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3]]), 0)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3]]), 0)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3]]), 0)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3]]), 0)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3]]), 0)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3]]), 0)
        self.assertEqual(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)


if __name__ == '__main__':
    unittest.main()