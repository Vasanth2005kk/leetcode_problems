class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 == 0:
            return n
        return n*2

n = 5
obj = Solution().smallestEvenMultiple(n)

print(obj)