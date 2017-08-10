class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            return x == int(str(x)[::-1])
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    a = raw_input("x = ")
    while str(a) != 'quit':
        print "Return", s.isPalindrome(int(a))
        a = raw_input("x = ")
