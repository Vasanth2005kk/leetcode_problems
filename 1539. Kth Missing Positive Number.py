from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        count  = 0
        value = 1
        while True:
            if value not in arr:
                count +=1 
            if count == k:
                return value
            value +=1

        
arr = [5,6,7,8,9]
k = 9

obj = Solution().findKthPositive(arr,k)

print(obj)