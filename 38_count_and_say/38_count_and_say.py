class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            last_string = self.countAndSay(n-1)
            current_num = last_string[0]
            num = 0
            this_string = ""
            for pos in range(len(last_string)):
                if last_string[pos] == current_num:
                    num += 1
                else:
                    this_string += str(num) + current_num
                    num = 1
                    current_num = last_string[pos]
            this_string += str(num) + current_num
            return this_string
