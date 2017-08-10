"""
Fail
Time Limit Exceeded
input = 2147483647
"""

from math import log

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            if x < 10:
                return True
            elif x <= 100:
                return x % 11 == 0
            else:
                if x % pow(10, int(log(x, 10))) != 0:
                    if (x % (pow(10, int(log(x, 10))) + 1)) % 10 == 0:
                        if  (x - (pow(10, int(log(x, 10))) + 1) * (x / (pow(10, int(log(x, 10))) + 1))) / 10 == 0:
                            return True
                        elif (x - (pow(10, int(log(x, 10))) + 1) * (x / (pow(10, int(log(x, 10))) + 1))) % pow(10,  int(log(x, 10)) - 1 - int(log((x - (pow(10, int(log(x, 10))) + 1) * (x / (pow(10, int(log(x, 10))) + 1))) / 10, 10))) == 0:
                            return self.isPalindrome((x - (pow(10, int(log(x, 10))) + 1) * (x / (pow(10, int(log(x, 10))) + 1))) / pow(10,  int(log(x, 10)) - 1 - int(log((x - (pow(10, int(log(x, 10))) + 1) * (x / (pow(10, int(log(x, 10))) + 1))) / 10, 10))))
        return False

if __name__ == "__main__":
    s = Solution()
    a = raw_input("x = ")
    while str(a) != 'quit':
        print "Return", s.isPalindrome(int(a))
        a = raw_input("x = ")
