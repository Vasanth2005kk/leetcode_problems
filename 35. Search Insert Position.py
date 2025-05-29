class Solution:
    def searchInsert(self, nums,target):
        nums+=[target]
        nums.sort()
        # print(nums)
        ouptut = nums.index(target)
        return ouptut
        
obj = Solution()

nums = [1,3,5,6]
target = 5

print(obj.searchInsert(nums, target))  # Output: 2