import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0

            maxVal = max(maxVal,node.val)

            res += dfs(node.left,maxVal)
            res += dfs(node.right,maxVal)

            return res

        return dfs(root,root.val)
        

class TestSolution(unittest.TestCase):

    def test_1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.left = TreeNode(3)
        root.right = TreeNode(4)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)
        self.assertEqual(Solution().goodNodes(root), 4)

    def test_2(self):
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(Solution().goodNodes(root), 3)

    def test_3(self):
        root = TreeNode(1)
        self.assertEqual(Solution().goodNodes(root), 1)


if __name__ == "__main__":
    unittest.main()