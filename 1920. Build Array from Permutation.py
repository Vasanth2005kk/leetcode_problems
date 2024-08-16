class Solution:
    def buildArray(self, nums):
        ans=[]
        for i in nums:
           ans+=[nums[i]]

        return ans
        

nums = [0,2,1,5,3,4]
obj = Solution().buildArray(nums=nums)

print(obj)