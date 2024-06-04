class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                
nums=[2,11,15,7]
target=9

obj=Solution()
output=obj.twoSum(nums=nums,target=target)
print(output)