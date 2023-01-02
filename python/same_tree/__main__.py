import unittest
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))


class TestSolution(unittest.TestCase):
    def test_isSameTree(self):
        solution = Solution()
        self.assertEqual(solution.isSameTree(TreeNode(1,TreeNode(2),TreeNode(3)),TreeNode(1,TreeNode(2),TreeNode(3))),True)
        self.assertEqual(solution.isSameTree(TreeNode(1,TreeNode(2)),TreeNode(1,None,TreeNode(2))),False)
        self.assertEqual(solution.isSameTree(TreeNode(1,TreeNode(2),TreeNode(1)),TreeNode(1,TreeNode(1),TreeNode(2))),False)

if __name__ == '__main__':

    unittest.main()