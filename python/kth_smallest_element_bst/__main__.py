from typing import Optional
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right



class Test(unittest.TestCase):
    def test_kthSmallest(self):
        solution = Solution()
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        self.assertEqual(solution.kthSmallest(root, 1), 1)
        self.assertEqual(solution.kthSmallest(root, 2), 2)
        self.assertEqual(solution.kthSmallest(root, 3), 3)
        self.assertEqual(solution.kthSmallest(root, 4), 4)


if __name__ == '__main__':
    unittest.main()