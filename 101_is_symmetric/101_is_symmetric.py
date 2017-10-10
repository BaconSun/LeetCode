# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isNodeSymmetric(self, p1, p2):
        if p1 == None and p2 == None:
            return True
        elif p1 != None and p2 != None:
            return p1.val == p2.val and self.isNodeSymmetric(p1.left, p2.right) and self.isNodeSymmetric(p1.right, p2.left)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isNodeSymmetric(root.left, root.right)
