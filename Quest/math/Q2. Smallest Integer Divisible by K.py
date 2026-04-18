
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:  
        if k % 2 != 0 and k % 5 != 0:
            n= 1
            step=1
            remainder = n % k 
            while remainder != 0:
                next = (remainder*10+1)
                remainder = next % k
                step +=1
            return step
        return -1



k = 99989
 
obj = Solution().smallestRepunitDivByK(k)

print(obj)