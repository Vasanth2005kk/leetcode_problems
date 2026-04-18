class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = list(range(1,n+1))
        total =  sum(nums)
        left = 0

        for i in nums:
            if left == total-left-i:
                return i
            else:
                left+=i
        return -1
    
n =  8
obj = Solution().pivotInteger(n)

print(obj)