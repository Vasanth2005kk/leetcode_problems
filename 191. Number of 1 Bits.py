class Solution:
    def hammingWeight(self, n: int) -> int:
        binarynumber = bin(n)
        bit_count = 0
        for i in binarynumber:
            if i == "1":
                bit_count+=1

        return bit_count



n=11

obj = Solution().hammingWeight(n)
print(obj)