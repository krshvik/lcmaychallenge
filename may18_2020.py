class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:    
        lens = len(s1)
        i = 0
        di = {}
        while i < lens:
            c = s1[i:i+1]
            i = i + 1
            if c in di:
                di[c] = di[c] + 1
            else:
                di[c] = 1
        
        len2 = len(s2)
        if len2 < lens:
            return False 
        i = 0 
        while i < len2:
            if s2[i:i+1] in di:
                t2 = s2[i:i+lens]
                if len(t2) < len(s1):
                    chk = 1
                else:
                    chk = 0 
                while chk == 0 and len(t2) > 0:
                    c = t2[:1]
                    if c in di:
                        if t2.count(t2[:1]) == di[t2[:1]]:
                            t2 = t2.replace(c,'')
                        else:
                            chk = 1
                    else:
                        chk = 1
                if chk == 0 and len(t2) == 0:
                    return True 
                
                i = i + 1                     
            else:
                i = i + 1
        return False 