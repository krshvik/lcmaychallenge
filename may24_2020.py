# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder == []:
            return None
        # print(preorder)
        root = TreeNode(preorder[0])
        lenp = len(preorder)
        i = 1
        while i < lenp and preorder[i] < root.val:
            i = i + 1 
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root 