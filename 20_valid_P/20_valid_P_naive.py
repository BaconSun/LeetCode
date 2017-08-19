# NOTE: Time Out

class Solution(object):
    former = ['(', '{', '[']
    later = [')', '}', ']']
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            # To Cope with the case that begin with the later parentheses
            if s[i] in Solution.later:
                return False
            if s[i] in Solution.former:
                # Counter is to count total number of the same former parentheses occurs
                # Deal with the case like [[]]
                counter = 1
                j = i + 1
                while j < len(s):
                    if s[j] == s[i]:
                        counter += 1
                    elif s[j] == Solution.later[Solution.former.index(s[i])]:
                        counter -= 1
                    if counter == 0:
                        break
                    j += 1
                # The total numbers of former and later parentheses are not match
                if counter != 0:
                    return False
                # Divide the string into two parts to solve
                return self.isValid(s[i+1:j]) and self.isValid(s[j+1:])
        return True

if __name__ == "__main__":
    s = Solution()
    while True:
        print s.isValid(str(raw_input("Input:")))
