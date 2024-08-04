class Solution:
    def rangeSum(self, nums, n: int, left: int, right: int) -> int:
        output=[]
        total=0
        mod = 10**9 + 7
        for i in range(len(nums)):
            total=nums[i]
            output.append(total)
            for j in range(i+1,len(nums)):
                total+=nums[j]
                output.append(total)
            total=0
        output.sort()
        return sum(output[left-1:right])% mod

nums = [1,2,3,4]
n = 4
left = 1
right = 5
obj=Solution().rangeSum(nums=nums,n=n,left=left,right=right)

print(obj)