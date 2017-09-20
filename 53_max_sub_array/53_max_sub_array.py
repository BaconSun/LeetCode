class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        current_maxsum = nums[0]
        for i in range(1, len(nums)):
            current_maxsum = max(nums[i], current_maxsum + nums[i])
            maxsum = max(maxsum, current_maxsum)
        return maxsum
