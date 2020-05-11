class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldc = image[sr][sc]
        if oldc == newColor:
            return image
        leni = len(image)
        arr = [[sr,sc]]
        while len(arr) > 0:
            temp = []
            for a in arr:
                image[a[0]][a[1]] = newColor
                if a[0]-1 > -1:
                    if image[a[0]-1][a[1]] == oldc:
                        temp.append([a[0]-1,a[1]])
                if a[0]+ 1 < leni:
                    if image[a[0]+1][a[1]] == oldc:
                        temp.append([a[0]+1,a[1]])
                if a[1]-1 > -1:
                    if image[a[0]][a[1]-1] == oldc:
                        temp.append([a[0],a[1]-1])
                if a[1] + 1 < len(image[a[0]]):
                    if image[a[0]][a[1]+1] == oldc:
                        temp.append([a[0],a[1]+1])
            arr = temp
            # print()
        return image 