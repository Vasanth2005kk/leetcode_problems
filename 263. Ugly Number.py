class Solution:
    def isUgly(self, n: int) -> bool:        
        if n == 0:
            return False

        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3

        return n == 1
n=14
obj = Solution().isUgly(n)

print(obj)
    

    

        

