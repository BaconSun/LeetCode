class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            x1 = 1
            x2 = 2
            for i in range(2,n):
                temp = x2
                x2 = x1 + x2
                x1 = temp
            return x2
