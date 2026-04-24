class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a > b:
            maxValue = a 
        else:
            maxValue = b

        factorCount = 0

        for i in range(1,maxValue+1):
            if a % i == 0 and b % i == 0:
                factorCount +=1
                # print(i)

        return factorCount

a = 885
b = 885

obj = Solution().commonFactors(a,b)
print(obj)