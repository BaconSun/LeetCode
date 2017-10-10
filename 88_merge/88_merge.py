class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        k = 0
        nums1[0:len(nums1)] = nums1[0:m]
        for i in range(n):
            if len(nums1) == 0 or nums2[i] >= nums1[len(nums1)-1]:
                nums1[len(nums1):len(nums1)] = nums2[i:n]
                return
            for j in range(k, len(nums1)):
                if nums2[i] < nums1[j]:
                    nums1[j:j] = nums2[i:i+1]
                    k = j
                    break
