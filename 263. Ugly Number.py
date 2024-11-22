class Solution:
    def isUgly(self, n: int) -> bool:        
        if n in [0,1]:
            return True

        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3

        return n == 1

    

    

        


