""" The most naive way"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

if __name__ == '__main__':
    s = Solution()
    print "Input: nums = [2,7,11,15], target = 9"
    print "Ans:", s.twoSum([2,7,11,15], 9)
