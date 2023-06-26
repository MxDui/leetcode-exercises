import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res =[]

        def dfs(node):
            if not node:
                res.append('N')
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')
        self.i = 0

        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

class Test(unittest.TestCase):
    def test_one(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)

        ser = Codec()
        deser = Codec()
        ans = deser.deserialize(ser.serialize(root))
        self.assertEqual(ans.val, root.val)
        self.assertEqual(ans.left.val, root.left.val)
        self.assertEqual(ans.right.val, root.right.val)
        self.assertEqual(ans.right.left.val, root.right.left.val)
        self.assertEqual(ans.right.right.val, root.right.right.val)

    def test_two(self):
        root = None

        ser = Codec()
        deser = Codec()
        ans = deser.deserialize(ser.serialize(root))
        self.assertEqual(ans, root)

    def test_three(self):
        root = TreeNode(1)

        ser = Codec()
        deser = Codec()
        ans = deser.deserialize(ser.serialize(root))
        self.assertEqual(ans.val, root.val)

if __name__ == "__main__":
    unittest.main()