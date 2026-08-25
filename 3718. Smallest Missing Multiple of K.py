from typing import List
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        count = 1
        while True:
            misNum = count*k 
            if misNum not in nums:
                return misNum
            count+=1

nums = [8,2,3,4,6]
k = 2

obj = Solution().missingMultiple(nums,k)
print(obj)