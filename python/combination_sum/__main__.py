from typing import List
import unittest


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res


class Test(unittest.TestCase):
    def test_combinationSum(self):
        solution = Solution()
        self.assertEqual(solution.combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(
            solution.combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        )
        self.assertEqual(solution.combinationSum([2], 1), [])
        self.assertEqual(solution.combinationSum([1], 1), [[1]])
        self.assertEqual(solution.combinationSum([1], 2), [[1, 1]])


if __name__ == "__main__":
    unittest.main()
