class Solution:
    def getConcatenation(self, nums):
        return nums+nums
        
nums = [1,2,1]
obj = Solution().getConcatenation(nums=nums)
print(obj)