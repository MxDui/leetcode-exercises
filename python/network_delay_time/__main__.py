from typing import List
import collections
import unittest
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
         
        for u , v, w in times:
            edges[u].append((v,w))

        minHeap = [(0,k)]
        visited = set()
        t = 0

        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t,w1)

            for n2,w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,(w1+w2,n2))

        return t if len(visited) == n else -1
class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_networkDelayTime_1(self):
        times = [[2,1,1],[2,3,1],[3,4,1]]
        n = 4
        k = 2
        self.assertEqual(self.sol.networkDelayTime(times, n, k), 2)

    def test_networkDelayTime_2(self):
        times = [[1,2,1],[2,1,3]]
        n = 2
        k = 2
        self.assertEqual(self.sol.networkDelayTime(times, n, k), 3)

    def test_networkDelayTime_3(self):
        times = [[1,2,1],[2,3,2],[1,3,2]]
        n = 3
        k = 1
        self.assertEqual(self.sol.networkDelayTime(times, n, k), 2)

    def test_networkDelayTime_4(self):
        times = [[1,2,1],[2,3,2],[1,3,4]]
        n = 3
        k = 1
        self.assertEqual(self.sol.networkDelayTime(times, n, k), 3)

    def test_networkDelayTime_5(self):
        times = [[1,2,1]]
        n = 2
        k = 2
        self.assertEqual(self.sol.networkDelayTime(times, n, k), -1)

if __name__ == '__main__':
    unittest.main()