from typing import List
import unittest

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start,end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1]=max(lastEnd,end)
            else:
                output.append([start,end])


        return output



class TestSolution(unittest.TestCase):
    def test_merge(self):
        self.assertEqual(Solution().merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(Solution().merge([[1,4],[4,5]]), [[1,5]])
        self.assertEqual(Solution().merge([[1,4],[2,3]]), [[1,4]])
        self.assertEqual(Solution().merge([[1,4],[0,4]]), [[0,4]])
        self.assertEqual(Solution().merge([[1,4],[0,1]]), [[0,4]])
        self.assertEqual(Solution().merge([[1,4],[0,0]]), [[0,0],[1,4]])
        self.assertEqual(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]), [[1,10]])


if __name__ == '__main__':
    unittest.main()