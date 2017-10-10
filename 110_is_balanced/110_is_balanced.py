# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        max_depth = 0
        to_visit_list = [root]
        while len(to_visit_list) != 0:
            new_list = []
            for i in to_visit_list:
                if i.left != None:
                    new_list.append(i.left)
                if i.right != None:
                    new_list.append(i.right)
            to_visit_list = new_list
            max_depth += 1
        return max_depth
