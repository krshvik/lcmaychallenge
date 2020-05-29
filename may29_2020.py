class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq= {}
        for p in prerequisites:
            a = p[0]
            b = p[1]
            if a not in preq:
                preq[a] = {}
            preq[a][b] = 1
        
        fini = {}
        i = 0 
        while i < numCourses:
            if i not in preq:
                fini[i] = 1
            i = i + 1
        
        while len(preq) > 0:
            dels= [] 
            for p in preq:
                for q in preq[p]:
                    if q in fini:
                        # del preq[p][q]
                        dels.append([p,q]) ##= dels + 1 
        
            if len(dels) == 0:
                return False
            else:
                for d in dels:
                    p = d[0]
                    q = d[1]
                    del preq[p][q]
                    if len(preq[p]) == 0:
                        del preq[p]
                        fini[p] = 1 
        return True