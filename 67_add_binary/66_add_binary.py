class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        increment = 0
        result = ""
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                result = str((int(a[i]) + int(b[j]) + increment) % 2) + result
                increment = (int(a[i]) + int(b[j]) + increment) / 2
                i -= 1
                j -= 1
            elif i >= 0:
                result = str((int(a[i]) + increment) % 2) + result
                increment = (int(a[i]) + increment) / 2
                i -= 1
            elif j >= 0:
                result = str((int(b[j]) + increment) % 2) + result
                increment = (int(b[j]) + increment) / 2
                j -= 1
        if increment == 1:
            result = str(1) + result
        return result
