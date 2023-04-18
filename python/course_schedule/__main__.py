from typing import List
import unittest
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(crs):
                if crs in visited:
                    return False
                if preMap[crs] == []:
                    return True

                visited.add(crs)

                for pre in preMap[crs]:
                    if not dfs(pre): return False
                    
                visited.remove(crs)
                preMap[crs] = []
                return True

        for crs in range(numCourses):
            if not dfs(crs) : return False
        return True



class TestSolution(unittest.TestCase):
    def test_1(self):
        numCourses = 2
        prerequisites = [[1,0]]
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), True)

    def test_2(self):
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), False)

    def test_3(self):
        numCourses = 3
        prerequisites = [[1,0],[1,2],[0,1]]
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), False)

    def test_4(self):
        numCourses = 3
        prerequisites = [[1,0],[1,2],[0,2]]
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), True)

    def test_5(self):
        numCourses = 3
        prerequisites = [[1,0],[2,1],[0,2]]
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), False)

    def test_6(self):
        numCourses = 4
        prerequisites = [[1,0],[2,1],[3,2],[0,3]]
        self.assertEqual(Solution().canFinish(numCourses, prerequisites), False)

 



if __name__ == '__main__':
    unittest.main()