
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        temp  =0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] >= nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums[-k]
    
nums = [3,2,3,1,2,4,5,5,6]
k = 4


obj = Solution().findKthLargest(nums,k)
print(obj)



# code 


'''class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]'
'''