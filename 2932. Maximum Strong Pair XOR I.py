from typing import List
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        length =  len(nums)

        MaxValue = 0
        for i in range(length):
            for j in range(i,length):
                if abs(nums[i] - nums[j]) <= min(nums[i],nums[j]):
                    XorValue = nums[i] ^ nums[j]
                # print(XorValue, type(XorValue))
                    if MaxValue <= XorValue:
                    # print("XOR VALUE :",XorValue)
                        MaxValue = XorValue

        return MaxValue


nums = [1,2,3,4,5]
nums = [10,100]
obj = Solution().maximumStrongPairXor(nums)
print(obj)