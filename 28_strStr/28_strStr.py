class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        i = 0
        while i < len(haystack) - len(needle) + 1:
            found = True
            j = 0
            while j < len(needle) and found:
                if haystack[i+j] != needle[j]:
                    found = False
                else:
                    j+=1
            if found:
                return i
            i+=1
        return -1
