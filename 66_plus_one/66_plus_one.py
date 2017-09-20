class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        digits[i] += 1
        increament = min(int(digits[i]/10),1)
        digits[i] = digits[i]%10
        i -= 1
        while i >= 0:
            digits[i] += increament
            increament = min(int(digits[i]/10),1)
            digits[i] = digits[i]%10
            i -= 1
        if increament > 0:
            digits[0:0] = [1]
        return digits
