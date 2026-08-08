from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        minConst =  min(costs)
        if minConst > coins:
            return 0
        if minConst == coins:
            return 1
    
        maxConst =  max(costs)

        k = maxConst -  minConst +1

        counts = [0]*k
        for i in costs:
            # print(i-minConst)
            index =  i - minConst
            counts[index] +=1 

        # print(counts)
        sortCosts = []
        for i in range(k):
            nums = i + minConst
            f = counts[i]
            sortCosts.extend([nums]*f)
        

        print("Sorted Costs array :",sortCosts)

        total = 0
        bars = 0

        for i in sortCosts:
            total += i
            if total <= coins:
                bars+=1

        return bars


costs = [1,3,2,4,1]
coins = 7

obj = Solution().maxIceCream(costs,coins)

print(obj)