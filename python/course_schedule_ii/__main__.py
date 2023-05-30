from typing import List
import unittest

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses)}

        for crs,pre in prerequisites:
            prereq[crs].append(pre)
        output = []
        visit,cycle =set(),set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return output        


class Test(unittest.TestCase):
    def test(self):
        numCourses = 2
        prerequisites = [[1,0]]
        out = [0,1]
        self.assertEqual(Solution().findOrder(numCourses,prerequisites),out)
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        out = [0,1,2,3]
        self.assertEqual(Solution().findOrder(numCourses,prerequisites),out)
        numCourses = 1
        prerequisites = []
        out = [0]
        self.assertEqual(Solution().findOrder(numCourses,prerequisites),out)
        numCourses = 2
        prerequisites = [[0,1],[1,0]]
        out = []
        self.assertEqual(Solution().findOrder(numCourses,prerequisites),out)
        numCourses = 3
        prerequisites = [[1,0],[1,2],[0,1]]
        out = []
        self.assertEqual(Solution().findOrder(numCourses,prerequisites),out)
        numCourses = 3
        prerequisites = [[1,0],[2,0],[0,2]]
        out = []
        self.assertEqual(Solution().findOrder(numCourses,prerequisites),out)
        numCourses = 8
        prerequisites = [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]
        out = []
        self.assertEqual(Solution().findOrder(numCourses,prerequisites),out)


if __name__ == '__main__':
    unittest.main()