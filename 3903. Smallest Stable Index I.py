from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        for i in range(n):
            score = max(nums[:i+1]) - min(nums[i::]) 
            if score <= k:
                return i
        return -1

nums = [5,0,1,4]
k = 3

obj = Solution().firstStableIndex(nums,k)
print(obj)