class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        else:
            l = 0
            r = x
            i = (l + r) / 2
            while i * i > x or (i+1) * (i+1) <= x:
                if i * i > x:
                    r = i - 1
                else:
                    l = i + 1
                i = (l + r) / 2
            return i
