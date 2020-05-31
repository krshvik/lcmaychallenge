class Solution:
    
    di = {}
    
    def minDistance(self, word1: str, word2: str) -> int:
        
        tw1 = word1
        tw2 = word2 
        
        # print(tw1,tw2)
        
        if word1 in self.di:
            if word2 in self.di[word1]:
                return self.di[word1][word2]
        
        if len(word1) == 0:
            if tw1 not in self.di:
                self.di[tw1] = {}
            self.di[tw1][tw2] = len(word2)
            return len(word2)
        
        if word1.find(word2) > -1:
            if tw1 not in self.di:
                self.di[tw1] = {}
            self.di[tw1][tw2] = len(word1)-len(word2)
            return self.di[tw1][tw2] #### len(word1)-len(word2)
        
        while word1[:1] == word2[:1]:
            word1 = word1[1:]
            word2 = word2[1:]
        
        lenw1 = len(word1)
        lenw2 = len(word2)
        
        while word1[lenw1-1:] == word2[lenw2-1:]:
            word1 = word1[:lenw1-1]
            word2 = word2[:lenw2-1]
            lenw1 = lenw1 - 1
            lenw2 = lenw2 - 1
        
        mops = max(len(word1),len(word2))
        #### trying delete now 
        ops = 1
        val = self.minDistance(word1[1:],word2)
        
        if val + ops < mops:
            mops = val + ops
            # print('delete',mops,tw1,tw2)
        #### trying to replace 
        ops = 1
        val = self.minDistance(word1[1:],word2[1:])
        
        if val + ops < mops:
            mops = val + ops
            # print('replace',mops,tw1,tw2)
        
        #### insert now 
        
        ops = 1
        val = self.minDistance(word1,word2[1:])
        
        if val + ops < mops:
            mops = val + ops
            # print('insert',mops,tw1,tw2)
        
        if tw1 not in self.di:
            self.di[tw1] = {}
        
        self.di[tw1][tw2] = mops
        return mops 
        