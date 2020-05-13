class Solution:
        
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if len(num) <= k:
            return "0"
        
        return str(int(self.addd(num,len(num)-k)))
        
    def addd(self,num,k):
        # print(num,k)
        
        if len(num) <= k:
            return num
        
        if k == 0:
            return ""        
        
        if k == 1:
            i = 0
            while num.find(str(i)) == -1:
                i = i + 1 
            # print(str(i),'came here')
            return str(i)
        
        lenn = len(num)
        i = 0 
        while num.find(str(i)) > lenn-k or num.find(str(i)) == -1:
            i = i + 1 
        
        f = num.find(str(i))
        
        return str(i) + self.addd(num[f+1:],k-1)
        
        