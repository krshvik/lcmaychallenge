class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        di = {}
        for n in nums:
            if n in di:
                del di[n]
            else:
                di[n] = 1
        
        for d in di:
            return d 