from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in set(nums1):
            if i in set(nums2):
                output.append(i)

        return output
    

obj = Solution()
print(obj.intersection([1,2,2,1], [2,2]))  # Output: [2]
print(obj.intersection([4,9,5], [9,4,9,8,4]))  # Output: [9,4] or [4,9]