class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        i = 0
        j = 0
        substr = s[i:j]
        while j < len(s):
            if s[j] in substr:
                i = s.find(s[j], i) + 1
            j+=1
            substr = s[i:j]
            max_len = max(max_len, len(substr))
        return max_len

if __name__ =="__main__":
    s = Solution()
    test = ["abcabcbb", "bbbbb", "pwwkew"]
    for string in test:
        print "Input:", string
        print "Ans:", s.lengthOfLongestSubstring(string)
