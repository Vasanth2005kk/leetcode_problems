
nums = [1,1,1,3,3,4,3,2,4,2]
class Solution:
    def containsDuplicate(self, nums):        
        if len(nums) !=  len(set(nums)):
            return True
        else:
            return False

obj = Solution().containsDuplicate(nums)

print(obj)