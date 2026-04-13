from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        output = []
        for i in range(len(nums)):
            if nums[i] ==  target:
                output.append(abs(i-start))

        return min(output)
    

obj = Solution()

nums = [1,2,3,4,5]
target = 5
start = 3

ans =  obj.getMinDistance(nums,target,start)

print(ans)