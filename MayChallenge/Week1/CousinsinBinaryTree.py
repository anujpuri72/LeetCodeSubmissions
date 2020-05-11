# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lookup(self, root: TreeNode, x: int):
        if (root == None):
            return -999999
        elif (root.val == x):
            return 0
        else:
            leftheight = self.lookup(root.left, x)+1
            rightheight = self.lookup(root.right, x)+1
            return max(leftheight, rightheight)

    def findp(self, root: TreeNode, x: int):
        if (root == None):
            return None
        elif ((root.right != None and root.right.val == x) or (root.left != None and root.left.val == x)):
            return root
        else:
            found = self.findp(root.right, x)
            if (found == None):
                found = self.findp(root.left, x)
            return found

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_height = self.lookup(root, x)
        y_height = self.lookup(root, y)
        x_baap = self.findp(root, x)
        # print(x_height,y_height)
        if(x_height == y_height):
            if ((x_baap.right != None and x_baap.right.val == y) or (x_baap.left != None and x_baap.left.val == y)):
                return False
            else:
                return True
        else:
            return False
