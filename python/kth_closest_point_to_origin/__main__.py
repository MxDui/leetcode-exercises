from typing import List
import unittest
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x,y in points:
            dist = (x**2)+(y**2)
            minHeap.append([dist,x,y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist,x,y=heapq.heappop(minHeap)
            res.append([x,y])

            k-=1


        return res


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(sorted(Solution().kClosest([[1,3],[-2,2]],1)),sorted([[-2,2]]))

    def test2(self):
        self.assertEqual(sorted(Solution().kClosest([[3,3],[5,-1],[-2,4]],2)),sorted([[3,3],[-2,4]]))

    def test3(self):
        self.assertEqual(sorted(Solution().kClosest([[6,10],[-3,3],[2,5],[0,2]],3)),sorted([[2,5],[0,2],[-3,3]]))
        


 



if __name__ == '__main__':
    unittest.main()
