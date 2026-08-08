from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        sortedheights =  sorted(heights)

        count = 0
        for i in range(len(heights)):
            if heights[i] != sortedheights[i]:
                count +=1

        # print(count)
        return count
    
heights = [1,1,4,2,1,3]

obj = Solution().heightChecker(heights)

print(obj)