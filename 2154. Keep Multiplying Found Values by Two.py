nums = [5,3,6,1,12]
original = 3

class Solution:
    def findFinalValue(self, nums,original):
        while original in nums:
            original = original*2
        return original
    
obj=Solution().findFinalValue(nums,original)

print(obj)