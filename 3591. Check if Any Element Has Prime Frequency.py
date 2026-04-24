from typing import List

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:  
        def isPrime(n):
            if n < 2:
                return False
            
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            
            return True
        for i in nums:
            numberCount =  nums.count(i)
            if  numberCount >= 2:
                if isPrime(numberCount):
                    return True
        
        return False
    
nums = [1,2,3,4,5,4]

obj = Solution().checkPrimeFrequency(nums)

print(obj)