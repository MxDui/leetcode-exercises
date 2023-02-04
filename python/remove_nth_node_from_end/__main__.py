from typing import Optional 
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


class Test(unittest.TestCase):

    def test_removeNthFromEnd(self):
        solution = Solution()
        l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
        result = solution.removeNthFromEnd(l1, 2)
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
