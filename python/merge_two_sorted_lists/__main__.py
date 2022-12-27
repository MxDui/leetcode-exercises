import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2) -> ListNode:

        dummy = ListNode()

        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


class TestSolution(unittest.TestCase):
    def main(self):
        # create test cases

        list1_2 = None
        list2_2 = ListNode(1)
        expected_output_2 = ListNode(1)
        list1_3 = ListNode(1, ListNode(3))
        list2_3 = ListNode(2, ListNode(4))
        expected_output_3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        list1_4 = ListNode(1, ListNode(3))
        list2_4 = ListNode(1, ListNode(3))
        expected_output_4 = ListNode(1, ListNode(1, ListNode(3, ListNode(3))))

        # create a Solution object
        sol = Solution()

        # test the mergeTwoLists method

        self.assertEqual(sol.mergeTwoLists(
            list1_2, list2_2), expected_output_2)
        self.assertEqual(sol.mergeTwoLists(
            list1_3, list2_3), expected_output_3)
        self.assertEqual(sol.mergeTwoLists(
            list1_4, list2_4), expected_output_4)


if __name__ == '__main__':
    unittest.main()
