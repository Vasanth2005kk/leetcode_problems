class Solution:
    def sortArrayByParity(self, nums):
        output = []

        for i in nums:
            if i % 2 == 1:
                output.append(i)
            else:
                output.insert(0, i)

        return output

nums = [3, 1, 2, 4]
solution = Solution()
result = solution.sortArrayByParity(nums)
print(result)  # Output: [2, 4, 3, 1]