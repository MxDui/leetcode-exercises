import unittest
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))

        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_isSubtree(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        self.assertEqual(self.sol.isSubtree(root, subRoot), True)

        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(0)
        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        self.assertEqual(self.sol.isSubtree(root, subRoot), False)


if __name__ == "__main__":
    unittest.main()