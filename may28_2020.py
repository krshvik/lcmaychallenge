class Solution:
    def countBits(self, num: int) -> List[int]:
        i = 0 
        ret = []
        while i <= num:
            b = str(bin(i)).count('1')
            ret.append(b)
            i = i + 1
        return ret 