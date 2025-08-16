from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a= set(nums)
        for i in range(0,max(nums)+2):
            if i not in a:
                # print(i)
                return i


nums = [3,0,1]

obj = Solution().missingNumber(nums)

print(obj)

