from typing import List
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        dic = {}
        
        for i in arr:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        print(dic)
        MaxNum = 0    
        for i in dic:
            Cn = dic[i]
            percentage = (Cn/n)*100
            if 25 <= percentage and MaxNum < percentage:
                MaxNum = percentage
                output = i

        return output         



arr = [1,2,3,3]

obj = Solution().findSpecialInteger(arr)
print(obj)