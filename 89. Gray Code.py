class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        if n == 1:
            return [0,1]
        GrCode = []
        for n in range(0,2**n):
            gray = n ^ (n >> 1)
            GrCode.append(gray)
        return GrCode
    

n =  3

obj = Solution().grayCode(n)

print(obj)