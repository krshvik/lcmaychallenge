class Solution:
    def frequencySort(self, s: str) -> str:
        di = {}
        while len(s) > 0:
            c = s[:1]
            ts = ''
            cc = 0
            v = s.find(c)
            while v > -1:
                ts = ts + c
                s = s[:v] + s[v+1:]
                v = s.find(c)
                cc = cc + 1 
            
            if cc in di:
                di[cc] = di[cc] + ts
            else:
                di[cc] = ts
        rs = ''
        while len(di) > 0:
            md = max(di)
            rs = rs + di[md]
            del di[md]
        return rs 