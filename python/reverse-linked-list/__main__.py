import unittest
from typing import List
from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None

        curr = head 

        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

class TestReverseList(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))).next.next.next.next.val, 1)
        self.assertEqual(Solution().reverseList(ListNode(1, ListNode(2))).next.val, 1)
        self.assertEqual(Solution().reverseList(ListNode(2, ListNode(1, ListNode(3, ListNode(4, ListNode(5)))))).next.next.next.next.val, 2)

if __name__ == '__main__':
    unittest.main()
    