# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        current = head.val
        p = head
        while p.next != None:
            if p.next.val == current:
                p.next = p.next.next
            else:
                current = p.next.val
                p = p.next
        return head
