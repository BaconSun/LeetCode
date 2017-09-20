class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        if target > nums[r]:
            return r + 1
        pos = int((r + l) / 2)
        while l < r:
            if target == nums[pos]:
                return pos
            elif target > nums[pos]:
                l = pos + 1
            else:
                r = pos
            pos = int((r + l) / 2)
        return pos
