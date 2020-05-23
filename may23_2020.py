class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ret = []
        lena = len(A)
        lenb = len(B)
        i = 0 
        j = 0 
        ret = []
        
        while i < lena and j < lenb:
            al = A[i][0]
            ar = A[i][1]
            
            bl = B[j][0]
            br = B[j][1]
            
            li = max(al,bl)
            ri = min(ar,br)
            
            if li <= ri:
                ret.append([li,ri])
                
                if li == al:
                    
                    if ri == ar:
                        
                        i = i + 1 
                        
                    else:
                        
                        j = j + 1 
                else:
                    
                    if ri == ar:
                        
                        i = i + 1
                        
                    else:
                        
                        j = j + 1
            else:
                
                if li == al:
                    
                    j = j + 1
                
                else:
                    
                    i = i + 1
            # print(i,j)
        return ret 
                    
                        
                        