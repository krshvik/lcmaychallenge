class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        
        lenp = len(p)
        i = 0
        
        di = {}
        
        while i < lenp:
            c = p[i:i+1]
            if c in di:
                di[c] = di[c] + 1
            else:
                di[c] = 1
            i = i + 1 
        
        lens = len(s)
        i = 0 
        while i < lens:
            c = s[i:i+1]
            d2 = {}
            f = -1
            if c in di:
                ti = i 
                j = 0 
                while j < lenp and s[ti:ti+1] in di:
                    di[s[ti:ti+1]] = di[s[ti:ti+1]] - 1
                    if di[s[ti:ti+1]] == 0:
                        del di[s[ti:ti+1]] 
                    if s[ti:ti+1] in d2:
                        d2[s[ti:ti+1]] = d2[s[ti:ti+1]] + 1
                    else:
                        d2[s[ti:ti+1]] = 1 
                    ti = ti + 1 
                    j = j + 1 
                f = ti
            # print(di,i)
                if len(di) == 0:
                    ret.append(i)
                    while s[ti:ti+1] == s[i:i+1]:
                        ti = ti + 1
                        i= i + 1
                        ret.append(i)
                    di = d2 
                    i = i + 1 
                else:
                    for c in d2:
                        if c not in di:
                            di[c] = d2[c]
                        else:
                            di[c] = di[c] + d2[c]
                    if s[f:f+1] not in di:
                        i = f + 1
                    else:
                        i = i + 1
            else:
                i = i + 1 
            
        return ret 
                            