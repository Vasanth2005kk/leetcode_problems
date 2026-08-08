from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in arr2:
            iCount = arr1.count(i)
            result.extend([i]*iCount)

        mis=[]
        for misnum in arr1:
            if misnum not in result:
                mis.append(misnum)

        result.extend(sorted(mis))
        return result
    
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

obj = Solution().relativeSortArray(arr1,arr2)
print(obj)