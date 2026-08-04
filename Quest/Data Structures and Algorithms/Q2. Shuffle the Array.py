from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(n):
            # output.append(nums[i])
            # output.append(nums[n])
            output.extend([nums[i],nums[n]])
            n+=1

        return output

nums = [2,5,1,3,4,7]
n = 3

obj = Solution().shuffle(nums,n)

print(obj)