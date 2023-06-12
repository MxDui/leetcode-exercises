from typing import List
import collections
import unittest
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}  
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

      
        res = 0
        visit = set()
        minH = [[0, 0]]  
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res
    
class Test(unittest.TestCase):
    
        def test_minCostConnectPoints(self):
            points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
            expected = 20
            sol = Solution()
            self.assertEqual(sol.minCostConnectPoints(points),expected)
    
        def test_minCostConnectPoints2(self):
            points = [[3,12],[-2,5],[-4,1]]
            expected = 18
            sol = Solution()
            self.assertEqual(sol.minCostConnectPoints(points),expected)
    
        def test_minCostConnectPoints3(self):
            points = [[0,0],[1,1],[1,0],[-1,1]]
            expected = 4
            sol = Solution()
            self.assertEqual(sol.minCostConnectPoints(points),expected)
    
        def test_minCostConnectPoints4(self):
            points = [[-1000000,-1000000],[1000000,1000000]]
            expected = 4000000
            sol = Solution()
            self.assertEqual(sol.minCostConnectPoints(points),expected)
    
        def test_minCostConnectPoints5(self):
            points = [[0,0]]
            expected = 0
            sol = Solution()
            self.assertEqual(sol.minCostConnectPoints(points),expected)

if __name__ == "__main__":
    unittest.main()