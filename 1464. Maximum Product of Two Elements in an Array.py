from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = 0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                value = (nums[i]-1)*(nums[j]-1)
                if value >=  max and i != j:
                    max = value
        return max


nums = [1,5,4,5]
obj = Solution().maxProduct(nums)

print(obj)