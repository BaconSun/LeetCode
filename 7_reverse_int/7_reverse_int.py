class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            n = int(str(x)[::-1])
            if n <= 2147483647:
                return n
        else:
            n = int(str(x)[:0:-1])
            if n <= 2147483648:
                return -n
        return 0

if __name__ == "__main__":
    s = Solution()
    a = raw_input("x = ")
    while str(a) != 'quit':
        print "Return", s.reverse(int(a))
        a = raw_input("x = ")
