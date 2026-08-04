from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        minValue = min(nums)
        maxValue = max(nums)

        output = []
        for i in range(minValue,maxValue+1):
            if i not in nums:
                output.append(i)

        return output

nums = [1,4,2,5]
obj = Solution().findMissingElements(nums)

print(obj)