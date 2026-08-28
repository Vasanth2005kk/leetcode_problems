from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = (window_sum - nums[i - k] )+ nums[i]

            if window_sum > max_sum:
                max_sum = window_sum

        return float(f"{max_sum / k:.5f}")
        
        


nums = [1,12,-5,-6,50,3]
k = 4

# nums = [-1]
# k = 1

obj = Solution().findMaxAverage(nums,k)
print(obj)