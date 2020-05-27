class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        graph = {}
        for i in range(1,N+1):
            graph[i] = {}
            
        for d in dislikes:
            p1 = d[0]
            p2 = d[1]
            
            if p1 not in graph:
                graph[p1] = {}
            graph[p1][p2] = 1
            
            if p2 not in graph:
                graph[p2] = {}
            graph[p2][p1] = 1
        color = {}
     
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            for nei in graph[node]:
                if not dfs(nei,c ^ 1):
                    return False
            return True
        
        for node in range(1,N+1):
            if node not in color:
                if not dfs(node):
                    return False
        return True
        
                            
                
            
