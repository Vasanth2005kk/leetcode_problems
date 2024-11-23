class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:   
        for i in nums[::]:
            if val == i:
                nums.remove(i)

        return len(nums)


nums = [0,1,2,2,3,0,4,2]
val = 2


obj = Solution().removeElement(nums,val)

print(obj)