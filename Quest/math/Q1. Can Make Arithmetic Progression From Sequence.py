from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sort_arr =  sorted(arr)
        difference  = sort_arr[1]-sort_arr[0]

        # print(difference)

        for i in range(len(arr)-1):
            if sort_arr[i]+difference == sort_arr[i+1]:
                continue
            else:
                return False
        return True 
    

arr = [3,5,1]
obj = Solution().canMakeArithmeticProgression(arr)


print(obj)