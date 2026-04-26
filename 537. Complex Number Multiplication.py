class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = num1.split('+')
        c, d = num2.split('+')
        
        a = int(a)
        b = int(b[:-1])  
        c = int(c)
        d = int(d[:-1])
        
        #ac - bd = (1×1) - (1×1) = 1 - 1 = 0
        real = a * c - b * d

        #ac - bd = (1×1) - (1×1) = 1 - 1 = 0
        imaginary = a * d + b * c
        
        return f"{real}+{imaginary}i"
    

num1 = "1+1i"
num2 = "1+1i"

obj = Solution().complexNumberMultiply(num1,num2)
print(obj)    