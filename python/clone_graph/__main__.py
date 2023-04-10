import unittest
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))

            return copy 

        return clone(node) if node else None
    

class TestSolution(unittest.TestCase):
    def assertNodesEqual(self, node1: Node, node2: Node, visited: set = None) -> None:
        if visited is None:
            visited = set()
        if node1 in visited:
            return
        visited.add(node1)
        self.assertEqual(node1.val, node2.val)
        self.assertEqual(len(node1.neighbors), len(node2.neighbors))
        for n1, n2 in zip(node1.neighbors, node2.neighbors):
            self.assertNodesEqual(n1, n2, visited)
        
    def test_cloneGraph(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2,node4]
        node2.neighbors = [node1,node3]
        node3.neighbors = [node2,node4]
        node4.neighbors = [node1,node3]
        copy1 = Node(1)
        copy2 = Node(2)
        copy3 = Node(3)
        copy4 = Node(4)
        copy1.neighbors = [copy2,copy4]
        copy2.neighbors = [copy1,copy3]
        copy3.neighbors = [copy2,copy4]
        copy4.neighbors = [copy1,copy3]
        self.assertNodesEqual(Solution().cloneGraph(node1),copy1)



if __name__ == '__main__':
    unittest.main()