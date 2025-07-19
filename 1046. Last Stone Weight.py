class Solution:
    def lastStoneWeight(self, stones) -> int:
        while len(stones) != 1:
            stones.sort()
            ans = stones[-1]-stones[-2]
            stones.pop()
            stones.pop()
            stones.append(ans)

        return stones[0]
    

stones = [2,7,4,1,8,1]
print(Solution().lastStoneWeight(stones))