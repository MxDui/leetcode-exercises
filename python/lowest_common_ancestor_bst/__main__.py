import unittest 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            


class TestSolution(unittest.case.TestCase):
    def test_lowestCommonAncestor(self):
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        self.assertEqual(Solution().lowestCommonAncestor(root, root.left, root.right).val, 6)
        self.assertEqual(Solution().lowestCommonAncestor(root, root.left, root.left.right).val, 2)


if __name__ == '__main__':
    unittest.main()