from typing import Optional
import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node,left,right):
            if not node:
                return True
            if not(node.val < right and node.val > left):
                return False

            return (valid(node.left,left,node.val) and 
            valid(node.right,node.val,right))

        return valid(root,float("-inf"),float("inf"))



class Test(unittest.TestCase):
    def test(self):
        root = TreeNode(2,TreeNode(1),TreeNode(3))
        self.assertEqual(Solution().isValidBST(root),True)
        root = TreeNode(5,TreeNode(1),TreeNode(4,TreeNode(3),TreeNode(6)))
        self.assertEqual(Solution().isValidBST(root),False)

if __name__ == "__main__":
    unittest.main()