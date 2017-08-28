class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        lcp = ""
        for i in range(min(list(len(n) for n in strs))):
            temp = strs[0][i]
            for j in strs:
                if j[i] != temp:
                    return lcp
            lcp += temp
        return lcp
