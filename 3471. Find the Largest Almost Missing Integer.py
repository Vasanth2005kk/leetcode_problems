from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        run = (n-k)+1

        uqValue = set(nums)

        dic = {}

        for u in uqValue:
            lindex = k
            for i in range(run):
                subArr = nums[i:lindex:]
                if u in subArr:
                    if u not in dic:
                        dic[u] = 1
                    else:
                        dic[u] +=1
                    print(u in subArr,u,subArr)     

                lindex += 1

        almax = -1
        for i in dic:
            if almax < i and dic[i] == 1:
                almax =  i

        return almax



nums = [0,0]
k = 1

obj = Solution().largestInteger(nums,k)
print(obj)