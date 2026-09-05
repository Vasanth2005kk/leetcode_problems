class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 0:
            return -1

        # prefix_max[i] = max(nums[0] ... nums[i])
        prefix_max = [0] * n
        prefix_max[0] = nums[0]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])

        # suffix_min[i] = min(nums[i] ... nums[n-1])
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])

        # Find first stable index
        for i in range(n):
            score = prefix_max[i] - suffix_min[i]

            if score <= k:
                return i

        return -1


nums = [5,0,1,4]
k = 3

obj = Solution().firstStableIndex(nums,k)

print(obj)