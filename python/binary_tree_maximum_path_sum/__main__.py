from typing import Optional
import unittest 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0 

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax,0)
            rightMax = max(rightMax,0)

            res[0] = max(res[0],root.val + leftMax + rightMax)

            return root.val + max(leftMax,rightMax)

        dfs(root)

        return res[0]
    
class Test(unittest.TestCase):
    def test_maxPathSum(self):
        s = Solution()
        self.assertEqual(s.maxPathSum(TreeNode(1,TreeNode(2),TreeNode(3))), 6)
        self.assertEqual(s.maxPathSum(TreeNode(-10,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))), 42)
        self.assertEqual(s.maxPathSum(TreeNode(-3)), -3)
        self.assertEqual(s.maxPathSum(TreeNode(-2,TreeNode(-1))), -1)

if __name__ == '__main__':
    unittest.main()