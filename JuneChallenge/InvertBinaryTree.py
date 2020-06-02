# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invert(self, root: TreeNode):
        if(root == None):
            return
        else:
            root.left, root.right = root.right, root.left
            self.invert(root.right)
            self.invert(root.left)
            return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        a = self.invert(root)
        return a
