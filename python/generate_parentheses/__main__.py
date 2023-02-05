from typing import List
import unittest

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0, 0)

        return res


class TestSolution(unittest.TestCase):
    def test_generateParenthesis(self):
        self.assertEqual(Solution().generateParenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
    
    def test_generateParenthesis2(self):
        self.assertEqual(Solution().generateParenthesis(1), ["()"])

    def test_generateParenthesis3(self):
        self.assertEqual(Solution().generateParenthesis(2), ["(())", "()()"])

if __name__ == '__main__':
    unittest.main()
    