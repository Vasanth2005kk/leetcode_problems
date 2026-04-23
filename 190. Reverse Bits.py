class Solution:
    def reverseBits(self, n: int) -> int:
        binaryValue = format(n, '032b')[::-1]
        
        return int(binaryValue, 2)
    
n = 43261596

obj  = Solution().reverseBits(n)
print(obj)