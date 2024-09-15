class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return eval(f"{num1}*{num2}")
        return str(int(num1)*int(num2))



num1 = "123"
num2 = "456"

obj = Solution().multiply(num1=num1,num2=num2)

print(obj)