n = 4
k = 4


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count =0
        Value = 0
        for i in range(1,n+1):
            if n % i == 0:
                count +=1
                if k == count :
                    Value = i
                    break
        
        if Value == 0:
            return -1
        return Value


