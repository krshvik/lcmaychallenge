class Solution:
    
    di = {}
    par = {}
    
    def __init__(self):
        self.di = {}
        self.par = {}
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.travel(root,0,-1)
        if x not in self.di:
            return False
        if y not in self.di:
            return False
        if self.di[x] == self.di[y]:
            if self.par[x] != self.par[y]:
                return True
        return False 
        
    def travel(self,cnode,lvl,parent):
        if cnode is None:
            return
        self.di[cnode.val] = lvl
        self.par[cnode.val] = parent
        self.travel(cnode.left,lvl+1,cnode.val)
        self.travel(cnode.right,lvl+1,cnode.val)
        return 