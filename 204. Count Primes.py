class Solution:
    def countPrimes(self, n: int) -> int: 
        if n <= 2:
            return (0)
        elif n == 3:
            return (1)
        elif n == 4 or n == 5:
            return (2)
        elif n == 6 or n == 7:
            return (3)
        else:
            primes = 2
            count =1
            while True:
                chack1 = (6*count-1)
                chack2 = (6*count+1)

                if chack1 < n or chack2 < n:
                    if chack1 < n:
                        primes+=1
                    if chack2 < n:
                        primes+=1
                else:
                    break
                count +=1
            return (primes)
n=10 #[2,3,5,7,11]
obj = Solution().countPrimes(n)
print(obj)