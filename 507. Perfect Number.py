class Solution:
    def checkPerfectNumber(self, num: int) -> bool:   
        half_num=num//2
        # print(half_num)
        count = 0
        for i in range(half_num,0,-1):
            if num%i == 0:
                count+=i
        # print(count)
        if count == num:
            return True
        else:
            return False


num = 120

obj = Solution().checkPerfectNumber(num)
print(obj)


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False  # Perfect numbers are positive and greater than 1

        divisors_sum = 1  # Start with 1 because it's always a divisor
        sqrt_num = int(num ** 0.5)

        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:  # Avoid adding the square root twice
                    divisors_sum += num // i

        return divisors_sum == num
