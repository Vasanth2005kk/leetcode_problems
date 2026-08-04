from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = nums + nums

        return output


nums = [1,2,1]
obj = Solution().getConcatenation(nums)