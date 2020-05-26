class Solution:
    
        
    def findMaxLength(self, nums: List[int]) -> int:
        lenn = len(nums)
        i = 0 
        maxi = 0
        di = {}
        di[0] = [0] 
        cou = 0         

        while i < lenn:

            if nums[i] == 0:
                cou = cou - 1
            else:
                cou = cou + 1
            if cou in di:
                di[cou].append(i)
            else:
                di[cou] = [i]
            i = i + 1                 

        for d in di:
            if d == 0:
                lenn2 = len(di[d])
                if lenn2 > 1:
                    val = di[d][lenn2-1] - di[d][0] + 1
                    if val > maxi:
                        maxi = val
            else:
                lenn2 = len(di[d])
                if lenn2 > 1:
                    val = di[d][lenn2-1] - di[d][0] 
                    if val > maxi:
                        maxi = val 
        return maxi 
            
            
