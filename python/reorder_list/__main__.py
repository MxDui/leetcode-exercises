from typing import Optional
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head, head.next
        # middle
        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        # rever second half
        while second:
            tmp = second.next 
            second.next = prev 
            prev = second 
            second = tmp

        # merge two lists
        first,second = head,prev

        while second:
            tmp1, tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first ,second = tmp1,tmp2

class TestSolution(unittest.TestCase):
    def test_reorderList(self):
        solution = Solution()

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        expected = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))

        solution.reorderList(head)

        self.assertTrue(self.is_linked_list_equal(head, expected))

    def test_reorderList2(self):
        solution = Solution()

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        expected = ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))

        solution.reorderList(head)

        self.assertTrue(self.is_linked_list_equal(head, expected))

    def is_linked_list_equal(self, l1, l2):
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return not l1 and not l2
        
if __name__ == '__main__':
    unittest.main()