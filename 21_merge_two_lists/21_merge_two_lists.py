# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        l_last = l
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                l_last.next = ListNode(l2.val)
                l2 = l2.next
            else:
                l_last.next = ListNode(l1.val)
                l1 = l1.next
            l_last = l_last.next
        l_last.next = l1 if l1 else l2
        return l.next
