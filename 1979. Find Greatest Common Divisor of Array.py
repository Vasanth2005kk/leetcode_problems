from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        maxValue = nums[0]
        minValue = nums[-1]
        for i in range(1,maxValue+1):
            if maxValue % i == 0 and minValue % i == 0:
                CommanFactor = i
            
        return CommanFactor
    
nums = [2,5,6,9,10]


obj = Solution().findGCD(nums)

print(obj)