class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        di = {}
        for p in points:
            d = (p[0]**2)+(p[1]**2)
            if d in di:
                di[d].append(p)
            else:
                di[d] = [p]
        ret = []
        while len(ret) < K:
            mind = min(di)
            ret = ret + di[mind] ##.append(di[mind])
            del di[mind]
        return ret 