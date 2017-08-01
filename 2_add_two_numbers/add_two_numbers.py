# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1.next
        p2 = l2.next
        increase = (l1.val+l2.val) > 9
        ans = ListNode((l1.val+l2.val) % 10)
        ans_tail = ans
        while (p1 != None or p2 != None):
            if p1 != None and p2 != None:
                val = p1.val + p2.val + increase
                increase = val > 9
                val %= 10
                ans_tail.next = ListNode(val)
                ans_tail = ans_tail.next
                p1 = p1.next
                p2 = p2.next
            elif p1 == None:
                val = p2.val + increase
                increase = val > 9
                val %= 10
                ans_tail.next = ListNode(val)
                ans_tail = ans_tail.next
                p2 = p2.next
            else:
                val = p1.val + increase
                increase = val > 9
                val %= 10
                ans_tail.next = ListNode(val)
                ans_tail = ans_tail.next
                p1 = p1.next
        if increase:
            ans_tail.next = ListNode(1)
        return ans

def print_listNode (l1):
    print l1.val,
    t1 = l1.next
    while t1 != None:
        print "->", t1.val,
        t1 = t1.next
    print

def num_to_list (n):
    p = ListNode(n%10)
    p_tail = p
    n /= 10
    while (n>0):
        p_tail.next = ListNode(n%10)
        p_tail = p_tail.next
        n /= 10
    return p

def list_to_num (p):
    n = p.val
    i = 10
    t = p.next
    while t != None:
        n += i*t.val
        i *= 10
        t = t.next
    return n

if __name__ == "__main__":
    s = Solution()
    for i in xrange(1000):
        for j in xrange(1000):
            if i+j != list_to_num(s.addTwoNumbers(num_to_list(i), num_to_list(j))):
                print "Fatal_Error:", i
                print_listNode(num_to_list(i))
                print list_to_num(num_to_list(i))
                print "Fatal_Error:", j
                print_listNode(num_to_list(j))
                print list_to_num(num_to_list(j))
                print_listNode(s.addTwoNumbers(num_to_list(i), num_to_list(j)))
                raw_input()
    print "Success"
