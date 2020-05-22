class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        cmatrix = []
        j = 0 
        while j < cols:
            i = 0 
            c = []
            while i < rows:
                c.append(matrix[i][j])
                i = i + 1 
            cmatrix.append(c)
            j = j + 1 
        
        print(matrix,cmatrix)
        di = {}
        i = 0 
        tote = 0 
        arr = []
        while i < rows:
            j = 0
            while j < cols:
                if matrix[i][j] == 1:
                    tote = tote + 1 
                    arr.append([i,j])
                j = j + 1
            i = i + 1
        
        size = 2
        while len(arr) > 0:
            tarr = []
            for a in arr:
                i = a[0]
                j = a[1]
                
                if i + size - 1 < rows and j+size-1 < cols and sum(matrix[i+size-1][j:j+size]) == size and sum(cmatrix[j+size-1][i:i+size]) == size:
                    tarr.append([i,j])
                    tote = tote + 1 
            arr = tarr
            size = size + 1 
        return tote 
            