import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_max_depth(self):
        root = TreeNode(3, TreeNode(9), TreeNode(
            20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_max_depth_2(self):
        root = TreeNode(1, TreeNode(2, TreeNode(
            3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
        self.assertEqual(self.solution.maxDepth(root), 4)


if __name__ == '__main__':

    unittest.main()
