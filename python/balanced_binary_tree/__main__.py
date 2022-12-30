import unittest
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)

            return [balanced, 1+max(left[1], right[1])]

        return dfs(root)[0]


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_is_balanced(self):
        root = TreeNode(3, TreeNode(9), TreeNode(
            20, TreeNode(15), TreeNode(7)))
        self.assertTrue(self.solution.isBalanced(root))

    def test_is_not_balanced(self):
        root = TreeNode(1, TreeNode(2, TreeNode(
            3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
        self.assertFalse(self.solution.isBalanced(root))


if __name__ == '__main__':

    unittest.main()
