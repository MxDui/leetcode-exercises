from typing import List
import unittest


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i,v in enumerate(t):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3


class TestSolution(unittest.TestCase):
    
    def test_mergeTriplets(self):
        self.assertEqual(Solution().mergeTriplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]), True)
        self.assertEqual(Solution().mergeTriplets([[1,3,4],[2,5,8]], [2,5,8]), True)
        self.assertEqual(Solution().mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]), True)
        self.assertEqual(Solution().mergeTriplets([[3,4,5],[4,5,6]], [3,2,5]), False)
        self.assertEqual(Solution().mergeTriplets([[1,3,4],[2,5,8]], [2,5,9]), False)
        self.assertEqual(Solution().mergeTriplets([[1,1,1]], [1,1,1]), True)
        self.assertEqual(Solution().mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,1,2]), False)
        self.assertEqual(Solution().mergeTriplets([[1,4,5],[2,3,8]], [2,4,5]), False)
        self.assertEqual(Solution().mergeTriplets([[1,3,4],[2,5,8]], [2,5,7]), False)
        self.assertEqual(Solution().mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,2,3]), True)
        self.assertEqual(Solution().mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,3,2]), False)
        self.assertEqual(Solution().mergeTriplets([[1,3,4],[2,5,8]], [2,5,6]), False)
        self.assertEqual(Solution().mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [2,5,3]), True)
        self.assertEqual(Solution().mergeTriplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [2,3,4]), True)

if __name__ == '__main__':
    unittest.main()