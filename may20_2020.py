# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    arr = []
    
    def __init__(self):
        self.arr = []
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.travel(root,k)
        # print(self.arr)
        return self.arr[k-1]
    
    def travel(self,cnode,k):
        if cnode is None:
            return
        if cnode.left is not None:
            self.travel(cnode.left,k)
        if len(self.arr) == k:
            return
        self.arr.append(cnode.val)
        if len(self.arr) == k:
            return
        if cnode.right is not None:
            self.travel(cnode.right,k)
        if len(self.arr) == k:
            return 