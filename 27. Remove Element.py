from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:   
        count = 0
        for i in nums:
            if i != val:
                count +=1
        return count

nums = [0,1,2,2,3,0,4,2]
val = 2


obj = Solution().removeElement(nums,val)

print(obj)