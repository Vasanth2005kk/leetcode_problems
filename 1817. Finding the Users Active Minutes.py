from typing import List
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0]*k
        dic = {}
        chacking = {}

        for i,j in logs:
            if  i not in dic:
                dic[i] = {j}
            else:
                value = dic[i]
                value.add(j)
                dic[i] = value
                
        for i in dic:
            value = 1 
            chack = len(dic[i]) 
            if chack in chacking:
                value = chacking[chack]
                value += 1
                chacking[chack] = value
            else:
                chacking[chack] = value
        else:
            for index in chacking:
                answer[index-1] =  chacking[index]

        return answer

logs = [[1,1],[2,2],[2,3]]
k = 4

obj = Solution().findingUsersActiveMinutes(logs,k)
print(obj)