# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        else:
            return self.subHasPathSum(root, sum)

    def subHasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            if sum == 0:
                return True
            else:
                return False
        else:
            if root.left != None and root.right != None:
                return self.subHasPathSum(root.left, sum-root.val) or self.subHasPathSum(root.right, sum-root.val)
            elif root.left != None:
                return self.subHasPathSum(root.left, sum-root.val)
            else:
                return self.subHasPathSum(root.right, sum-root.val)
