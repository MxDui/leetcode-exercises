from typing import List
import unittest
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(cur,pos,target):
            if target == 0:
                res.append(cur.copy())
            elif target <= 0:
                return
            prev = -1
            for i in range(pos,len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur,i+1,target - candidates[i])
                cur.pop()
                prev = candidates[i]
        backtrack([],0,target)
        return res
    
class TestSolution(unittest.TestCase):

    def test_1(self):
        candidates = [10,1,2,7,6,1,5]
        target = 8
        self.assertEqual(Solution().combinationSum2(candidates,target), [[1,1,6],[1,2,5],[1,7],[2,6]])

    def test_2(self):
        candidates = [2,5,2,1,2]
        target = 5
        self.assertEqual(Solution().combinationSum2(candidates,target), [[1,2,2],[5]])

    def test_3(self):
        candidates = [1,2,3]
        target = 6
        self.assertEqual(Solution().combinationSum2(candidates,target), [[1,2,3]])


if __name__ == "__main__":
    unittest.main()