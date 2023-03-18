from typing import List, Optional
import unittest
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)


            if rightSide:
                res.append(rightSide.val)
        
        return res
            

class Test(unittest.TestCase):
    def test(self):
        root = TreeNode(1,TreeNode(2,TreeNode(4)),TreeNode(3,None,TreeNode(5)))
        self.assertEqual(Solution().rightSideView(root),[1,3,5])

        root = TreeNode(1,None,TreeNode(3))
        self.assertEqual(Solution().rightSideView(root),[1,3])

        root = TreeNode(1)
        self.assertEqual(Solution().rightSideView(root),[1])

        root = TreeNode(1,TreeNode(2))
        self.assertEqual(Solution().rightSideView(root),[1,2])


if __name__ == "__main__":
    unittest.main()