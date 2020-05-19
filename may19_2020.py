class StockSpanner:
    
    arr = []
    lena = 0 
    di = {}
    
    def __init__(self):
        self.arr = []
        self.lena = 0 
        self.di = {}
        
    def next(self, price: int) -> int:
        
        
        self.lena = self.lena + 1 
        
        if price not in self.di:
            self.di[price] = self.lena 
        
        if self.arr == []:
            self.arr.append(price)
            self.di[price] = self.lena
            return 1 
        
        if price < self.arr[0]:
            self.arr = [price] + self.arr
            self.di[price] = self.lena
            return 1 
                
        if price > self.arr[len(self.arr)-1]:
            self.arr.append(price)
            self.di[price] = self.lena 
            return self.lena
        
        if price == self.arr[len(self.arr)-1]:
            self.di[price] = self.lena 
            return self.lena
        
        ind = self.bsearch(self.arr,0,len(self.arr)-1,price)

        if ind == -1:
            self.arr.append(price)
            self.di[price] = self.lena 
            return len(self.arr)

        posi = ind
        
        cpos = 0
        pincl = 1
        if self.arr[ind] == price:
            pincl = pincl - 1 
            
        lena = len(self.arr)
        while ind < lena:
            if self.arr[ind] != price and self.di[self.arr[ind]] > cpos:
                cpos = self.di[self.arr[ind]]
            ind = ind + 1
        
        if self.arr[posi] != price:
            self.arr = self.arr[:posi] + [price] + self.arr[posi:]
        self.di[price] = self.lena 
        return self.lena-cpos
        
    def bsearch(self,arr,l,r,val):
        # print(arr,l,r,val)
        
        if l == r-1:
            if val < arr[l]:
                return l
            if val == arr[l]:
                return l   
            if val < arr[r]:
                return r
            return r + 1 
        
        if l == r:
            if val <= arr[l]:
                return l
            return l + 1 
        
        mid = int((l+r)//2)
        
        if arr[mid] == val:
            return mid
        
        if arr[mid] > val:
            return self.bsearch(arr,l,mid-1,val)
        
        return self.bsearch(arr,mid+1,r,val)
        
        
