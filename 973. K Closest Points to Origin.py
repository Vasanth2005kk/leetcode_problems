from typing import List
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dic = {}

        for index,i in enumerate(points,0):
            x = i[0]**2
            y = i[1]**2
            dic[index] = x+y 

        sorted_by_key = dict(sorted(dic.items(),key=lambda item: item[1]))
        # print(sorted_by_key)

        output = []
        count = 0
        for i in sorted_by_key:
            if count == k:
                break
            output.append(points[i])            
            count+=1

        return output

points = [[1,3],[-2,2],[2,-2]]
k = 2

obj = Solution().kClosest(points,k)
print(obj)