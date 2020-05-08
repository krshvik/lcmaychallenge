class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slopes = {}
        c = {}
        
        lenc = len(coordinates)
        
        if lenc == 2:
            return True
        i = 0 
        
        inf = 0
        
        while i < lenc-1:
            j = i + 1
            x1 = coordinates[i][0]
            y1 = coordinates[i][1]
            while j < lenc:
                x2 = coordinates[j][0]
                y2 = coordinates[j][1]
                
                if x1 == x2:
                    if len(slopes) > 1:
                        return False 
                    slopes['inf'] = 1
                else:
                    if 'inf' in slopes:
                        return False 
                    else:
                        slopea = y2-y1
                        slopeb = x2-x1
                        
                        if len(slopes) == 1:
                            mina = min(slopes)
                            minb = min(slopes[mina])
                    
                            if slopea/slopeb != mina/minb:
                                return False 
                        else:
                            slopes[slopea] = {} ##1
                            slopes[slopea][slopeb] = 1 
                        
                j = j + 1
            i = i + 1 
        return True 
                    