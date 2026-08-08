from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citationsSort = sorted(citations,reverse=True)
        print("desc order :",citationsSort)

        count = 0
        for i in range(len(citations)):
            if citationsSort[i] >= i+1:
                count +=1

        return count


citations = [3,0,6,1,5]
obj = Solution().hIndex(citations)

print(obj)