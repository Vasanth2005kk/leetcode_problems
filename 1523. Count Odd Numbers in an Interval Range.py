class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = ( (high-low + 1)+(low%2))//2
        return count

low = 8
high = 10
obj = Solution().countOdds(low,high)

print(obj)