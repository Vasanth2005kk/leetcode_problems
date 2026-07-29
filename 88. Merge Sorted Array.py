from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while len(nums1) != m:
            nums1.pop()
        for i in range(n):
            nums1.append(nums2[i])

        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                if nums1[i] > nums1[j]:
                    nums1[i] , nums1[j] = nums1[j] , nums1[i]

        return nums1
        
nums1 = [2,0]
m = 1
nums2 = [1]
n = 1

obj = Solution().merge(nums1=nums1,
                       m=m,
                       nums2=nums2,
                       n=n)

print(obj)