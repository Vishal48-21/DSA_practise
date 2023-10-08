class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nd = 0
        dv = 0
        for  i in range(1,n+1):
            if i%m == 0:
                dv += i
            else:
                nd += i
        return nd-dv
        
