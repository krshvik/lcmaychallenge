class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusts = {}
        trusted = {}
        for t in trust:
            a = t[0]
            b = t[1]
            
            if a in trusts:
                trusts[a].append(b)
            else:
                trusts[a] = [b]
            
            if b in trusted:
                trusted[b].append(a)
            else:
                trusted[b] = [a]
        if N == 1:
            return 1 
        i = 1
        while i <= N:
            if i not in trusts:
                if i in trusted:
                    if len(trusted[i]) == N-1:
                        return i
            i = i + 1
        return -1