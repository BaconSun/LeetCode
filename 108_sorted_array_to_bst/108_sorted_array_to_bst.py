# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        i = int(len(nums) / 2.0)
        node = TreeNode(nums[i])
        node.left = self.sortedArrayToBST(nums[0:i])
        node.right = self.sortedArrayToBST(nums[i+1:])
        return node
