# Definition for a binary tree node.
# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.l=[]
        
    def printInorder(self,root): 
        if root: 
            self.printInorder(root.left) 
            self.l.append(root.val)
            self.printInorder(root.right)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.l=[]
        self.printInorder(root)
        return (self.l[k-1])
        
        
        