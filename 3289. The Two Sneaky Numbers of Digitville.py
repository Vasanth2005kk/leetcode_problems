from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        uinc = []
        output=[]
        for i in nums:
            if i not in uinc:
                uinc.append(i)
            else:
                output.append(i)

        return output

nums = [7,1,5,4,3,4,6,0,9,5,8,2]

obj = Solution().getSneakyNumbers(nums)

print(obj)