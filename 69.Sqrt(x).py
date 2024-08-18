class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        return int(math.sqrt(x)) # or int(x**0.5)

x = 4

obj=Solution().mySqrt(x)

print(obj)