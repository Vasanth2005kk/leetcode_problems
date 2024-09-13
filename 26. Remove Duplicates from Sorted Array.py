class Solution:
    def removeDuplicates(self, nums):
        sort_1=[]
        sort_2=[]

        for i in nums:
            if i not in sort_1:
                sort_1.append(i)
            else:
                sort_2.append(i)

        for j in sort_2:
            nums.remove(j)

        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]

obj=Solution().removeDuplicates(nums=nums)
print(obj)