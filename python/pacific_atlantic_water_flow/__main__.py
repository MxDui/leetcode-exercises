from typing import List
import unittest

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])

        pac,atl = set(),set()

        def dfs(r,c,visit,prevHeight):
            if((r,c) in visit or r<0 or c<0 or r==rows or c == cols or heights[r][c]<prevHeight):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows -1,c,atl,heights[rows -1][c])

        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols - 1,atl,heights[r][c])

        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])


        return res


class Test(unittest.TestCase):
    def test_pacificAtlantic(self):
        sol = Solution()

        # Test case 1
        heights = [[1,2,2,3,5],
                [3,2,3,4,4],
                [2,4,5,3,1],
                [6,7,1,4,5],
                [5,1,1,2,4]]
        expected_output = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        self.assertEqual(sol.pacificAtlantic(heights), expected_output)

        # Test case 2
        heights = [[1,2,3],
                [8,9,4],
                [7,6,5]]
        expected_output = [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        self.assertEqual(sol.pacificAtlantic(heights), expected_output)

     



if __name__ == '__main__':
    unittest.main()