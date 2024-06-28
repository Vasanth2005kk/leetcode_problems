class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array=nums1+nums2
        merged_array.sort()
        if len(merged_array) == 1:
            return merged_array[0]
        elif len(merged_array)%2 == 0:
            ans=merged_array[int(len(merged_array)/2)-1]+merged_array[int(len(merged_array)/2)]
            if ans/2 <0:
                return int(ans/2)
            return ans/2
        else:
            return merged_array[int((len(merged_array)+1)/2)-1]

nums1 = [1,2]
nums2 = [3,4]

obj=Solution()
output=obj.findMedianSortedArrays(nums1,nums2)

print(output)