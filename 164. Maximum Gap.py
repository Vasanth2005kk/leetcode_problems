from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        numsLength = len(nums)
        if numsLength > 1:
            nums.sort()
            maxValue  = 0
            for index in range(numsLength-1):
                value =  abs(nums[index] - nums[index+1])
                if maxValue < value:
                    maxValue =  value

            return maxValue
        
        return 0

nums =  [3,6,9,1]
obj = Solution().maximumGap(nums)

print(obj)