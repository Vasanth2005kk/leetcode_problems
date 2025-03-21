n =19

class Solution:
    def isHappy(self, n: int) -> bool:        
        while n != 0:
            value =0
            for i in str(n):
                value += int(i)**2
            n=value
            # print(n)
            if n in range(2,7):
                return  False
            elif n == 1:
                return True
        else:
            return True

n= 1111111
obj = Solution().isHappy(n)

print(obj)