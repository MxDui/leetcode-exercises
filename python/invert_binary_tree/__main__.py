
import unittest


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


class TestInvertTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_invert_tree(self):
        # Test basic case
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        inverted_root = self.solution.invertTree(root)
        self.assertEqual(inverted_root.val, 4)
        self.assertEqual(inverted_root.left.val, 7)
        self.assertEqual(inverted_root.right.val, 2)
        self.assertEqual(inverted_root.left.left.val, 9)
        self.assertEqual(inverted_root.left.right.val, 6)
        self.assertEqual(inverted_root.right.left.val, 3)
        self.assertEqual(inverted_root.right.right.val, 1)

        # Test case with empty tree
        empty_root = self.solution.invertTree(None)
        self.assertIsNone(empty_root)


if __name__ == '__main__':
    unittest.main()
