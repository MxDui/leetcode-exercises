from typing import Optional
import unittest

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None}

        cur = head

        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
            
        return oldToCopy[head]
    

class TestSolution(unittest.TestCase):
    def test_copyRandomList(self):
        solution = Solution()

        head = Node(7, Node(13, Node(11, Node(10, Node(1))))) 
        head.random = None
        head.next.random = head
        head.next.next.random = head.next.next.next.next
        head.next.next.next.random = head.next.next.next.next
        head.next.next.next.next.random = head

        expected = Node(7, Node(13, Node(11, Node(10, Node(1)))))
        expected.random = None
        expected.next.random = expected
        expected.next.next.random = expected.next.next.next.next
        expected.next.next.next.random = expected.next.next.next.next
        expected.next.next.next.next.random = expected

        

        result = solution.copyRandomList(head)

        self.assertTrue(self.is_linked_list_equal(result, expected))

    def is_linked_list_equal(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return not l1 and not l2
    

if __name__ == '__main__':
    unittest.main()