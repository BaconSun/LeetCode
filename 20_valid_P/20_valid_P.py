class Solution(object):
    former = ['(', '{', '[']
    later = [')', '}', ']']
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        k = []
        for i in s:
            if i in Solution.former:
                k.append(i)
            if i in Solution.later:
                if len(k) == 0:
                    return False
                if k.pop() != Solution.former[Solution.later.index(i)]:
                    return False
        if len(k) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    while True:
        print s.isValid(str(raw_input("Input:")))
