from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n-1):
            if (sum(nums[0:i+1]) - sum(nums[i+1:])) % 2 == 0:
                total += 1 

        return total


nums = [10,10,3,7,6]
obj = Solution().countPartitions(nums)
print(obj)
nums = [1,2,2]
obj = Solution().countPartitions(nums)
print(obj)
nums = [2,4,6,8]
obj = Solution().countPartitions(nums)
print(obj)
