from typing import List
import unittest

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


class TestSolution(unittest.TestCase):
    
        def test_1(self):
            edges = [[1, 2], [1, 3], [2, 3]]
            self.assertEqual(Solution().findRedundantConnection(edges), [2, 3])
    
        def test_2(self):
            edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
            self.assertEqual(Solution().findRedundantConnection(edges), [1, 4])

        
if __name__ == "__main__":
    unittest.main()