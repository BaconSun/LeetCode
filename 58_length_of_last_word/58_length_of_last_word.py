class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        while i >= 0:
            if s[i] == " ":
                i -= 1
            else:
                break
        if i < 0:
            return 0
        else:
            j = i
            while j >= 0:
                if s[j] != " ":
                    j -= 1
                else:
                    break
            return i - j
