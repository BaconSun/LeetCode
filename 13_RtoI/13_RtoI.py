class Solution(object):
    char_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                sum += Solution.char_dict[s[i]]
            elif Solution.char_dict[s[i]] >= Solution.char_dict[s[i+1]]:
                sum += Solution.char_dict[s[i]]
            else:
                sum -= Solution.char_dict[s[i]]
        return sum

if __name__ == "__main__":
    s = Solution()
    input = ["CXCIX"]
    for i in input:
        print "input:", i
        print "output:", s.romanToInt(i)
