class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if -2147483648 == dividend and -1 == divisor :
            return 2147483647
        else:

            return int(dividend/divisor)

dividend = 10
divisor = 3

obj = Solution().divide(dividend=dividend,divisor=divisor)
print(obj)