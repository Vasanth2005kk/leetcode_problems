from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i]**2

        return sorted(nums)

nums = [-4,-1,0,3,10]
obj = Solution().sortedSquares(nums)

print(obj)