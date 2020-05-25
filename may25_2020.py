class Solution:
    
    found = {}
    lena = 0
    lenb = 0 
    
    def __init__(self):
        self.found = {}
        self.lena = 0 
        self.lenb = 0 
        
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
                
        self.lena = len(A)
        self.lenb = len(B)
        return self.cross(0,0,A,B)
    def cross(self,ai,bi,A,B):
        
        maxi = 0 
        if ai in self.found and bi in self.found[ai]:
            return self.found[ai][bi]
        
        ai2 = ai
        bi2 = bi 
        
        di = {}
        while bi < self.lenb:
            if B[bi] in di:
                di[B[bi]].append(bi)
            else:
                di[B[bi]] = [bi]
            bi = bi + 1 
        
        i = 0 
        tmaxi = 0 
        while ai < self.lena:
            if A[ai] in di:
                indi = di[A[ai]][0]
                # print(i,indi,lena,lenb)
                max2 = self.cross(ai+1,indi+1,A,B) + 1 
                max3 = self.cross(ai+1,bi,A,B)
                ma = max(max2,max3)
                if ma > tmaxi:
                    tmaxi = ma
            ai = ai + 1
        
        if ai2 not in self.found:
            self.found[ai2] = {}
        self.found[ai2][bi2] = tmaxi 
        
        return tmaxi  