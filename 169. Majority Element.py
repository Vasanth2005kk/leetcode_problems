class Solution:
    def majorityElement(self, nums):
        chacking  = 0
        output = 0
        for i in set(nums):
            NumberCount = nums.count(i)
            # print(NumberCount)
            if chacking < NumberCount :
                chacking = NumberCount
                output = i
        return output


obj = Solution()
nums = [2,2,1,1,1,2,2]

print(obj.majorityElement(nums))  # Output: 2