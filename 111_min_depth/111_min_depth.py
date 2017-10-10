# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        min_depth = 0
        to_visit_list = [root]
        end = False
        while len(to_visit_list) != 0 and not end:
            min_depth += 1
            new_list = []
            for i in to_visit_list:
                if i.left == None and i.right == None:
                    end = True
                    break
                if i.left != None:
                    new_list.append(i.left)
                if i.right != None:
                    new_list.append(i.right)
            to_visit_list = new_list
        return min_depth
