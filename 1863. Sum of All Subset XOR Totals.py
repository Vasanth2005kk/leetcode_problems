class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        for i in range(2**n):
            XOR_total   = 0
            for j in range(n):
                if (i >> j)  & 1:
                    XOR_total ^= nums[j]
            result += XOR_total

        print(result)



'''
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_or = 0
        for num in nums:
            total_or |= num  # bitwise OR of all numbers
        n = len(nums)
        return total_or * (1 << (n - 1))

'''