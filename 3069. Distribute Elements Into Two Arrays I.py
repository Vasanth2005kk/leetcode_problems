from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = []
        arr2 = []

        for i in range(n):
            if len(arr1)==0:
                arr1.append(nums[i])
                continue
            elif len(arr2) ==0:
                arr2.append(nums[i])
                continue

            if (len(arr1) != 0 and len(arr2) !=0) and (arr1[-1] > arr2[-1]):
                    arr1.append(nums[i])
            elif (len(arr1) != 0 and len(arr2) !=0) and (arr1[-1] < arr2[-1]):
                    arr2.append(nums[i])


        return arr1+arr2




nums = [1,2,4]
obj = Solution().resultArray(nums)
print(obj)