class Solution:
    def singleNumber(self, nums) -> int:
        
        if len(nums) == 1:
            return nums[0]
        else:
            d=[]
            check_value=[]

            for i in nums:
                if i in d:
                    check_value.append(i)
                else:
                    d.append(i)

            for i in nums:
                if i not in check_value:
                    return i
                

nums=[2,2,1]
obj=Solution().singleNumber(nums=nums)
print(obj)