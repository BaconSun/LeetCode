# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        reverse_list = []
        to_visit_list = [root]
        while len(to_visit_list) != 0:
            value_list = []
            new_visit_list = []
            for i in to_visit_list:
                value_list.append(i.val)
                if i.left != None:
                    new_visit_list.append(i.left)
                if i.right != None:
                    new_visit_list.append(i.right)
            to_visit_list = new_visit_list
            reverse_list[0:0] = [value_list]
        return reverse_list
