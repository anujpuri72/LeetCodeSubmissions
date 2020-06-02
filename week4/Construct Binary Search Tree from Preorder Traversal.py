# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def construct(self, pre: List[int], start, end, orig):
        if(start > end):
            return None
        orig.val = pre[start]
        i = start
        while(i <= end):
            if(pre[i] > orig.val):
                break
            i += 1
        orig.left = self.construct(pre, start+1, i-1, TreeNode())
        orig.right = self.construct(pre, i, end, TreeNode())
        return orig

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        b = self.construct(preorder, 0, len(preorder)-1, TreeNode())
        return b
