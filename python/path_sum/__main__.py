from typing import Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val

        leftSum = self.hasPathSum(root.left, targetSum - root.val)
        rightSum = self.hasPathSum(root.right, targetSum - root.val)

        return leftSum or rightSum
    
class Test(unittest.TestCase):
    def test(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        targetSum = 22
        out = True
        self.assertEqual(Solution().hasPathSum(root, targetSum), out)
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        targetSum = 5
        out = False
        self.assertEqual(Solution().hasPathSum(root, targetSum), out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)




        

        