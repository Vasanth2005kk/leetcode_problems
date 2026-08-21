from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        def count_le(x: int) -> int:
            total = 0
            for mask in range(1, 1 << n):
                l = 1
                bits = 0
                for i in range(n):
                    if mask & (1 << i):
                        l = lcm(l, coins[i])
                        bits += 1
                        if l > x:  
                            break
                if l <= x:
                    term = x // l
                    if bits % 2 == 1:
                        total += term
                    else:
                        total -= term
            return total

        lo, hi = min(coins), min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo


coins = [11,5,12,17]
k = 87103

coins = [3,6,9]
k = 3

coins = [5,2]
k = 7

obj = Solution().findKthSmallest(coins,k)
print(obj)