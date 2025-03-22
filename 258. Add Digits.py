class Solution:
    def addDigits(self, num: int) -> int:       
        while num >= 10:
            value =0
            for i in str(num):
                value += int(i)

            num = value

            if num <= 9:
                return num
        else:
            return num
num = 32
obj = Solution().addDigits(num)

print(obj)