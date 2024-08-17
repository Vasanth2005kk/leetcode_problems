class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in stones:
            if i in jewels:
                count+=1
        return count
    
jewels = "aA"
stones = "aAAbbbb"
obj=Solution().numJewelsInStones(jewels,stones)

print(obj)