from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0 
        minValue = 100000000000
        Sumsub  = 0

        while right < len(nums):
            Sumsub += nums[right]
            while Sumsub >= target:
                minValue = min(minValue,right-left+1)
                Sumsub-=nums[left]
                left +=1
            right +=1

        return 0 if minValue == 100000000000 else minValue

target = 7
nums = [2,3,1,2,4,3]

obj = Solution().minSubArrayLen(target,nums)
print(obj)