from typing import List
import unittest

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()

        def dfs(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in visit):
                return 0

            visit.add((r,c))

            return (1 + dfs(r+1,c)+
                        dfs(r-1,c)+
                        dfs(r,c+1)+
                        dfs(r,c-1))

        area = 0
        for r in range(rows):
            for c in range(cols):
                 area = max(area,dfs(r,c))

        return area



class TestSolution(unittest.TestCase):
    def test_maxAreaOfIsland(self):
        self.assertEqual(Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                                    [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                                    [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                                    [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                                    [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                                    [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                                    [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                                    [0,0,0,0,0,0,0,1,1,0,0,0,0]]), 6)
        self.assertEqual(Solution().maxAreaOfIsland([[0,0,0,0,0,0,0,0]]), 0)

        self.assertEqual(Solution().maxAreaOfIsland([[1,1,0,0,0], [1,1,0,0,0], [0,0,0,1,1], [0,0,0,1,1]]), 4)


if __name__ == '__main__':
    unittest.main()
