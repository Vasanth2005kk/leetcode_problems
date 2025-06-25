class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i=1
        result = 0
        while True:
            if n == 1:
                return True
            elif n%2 != 1:
                return False
            else:
                result = 3**i
                if result == n:
                    return True
                elif result > n:
                    return False
                else:
                    i+=1