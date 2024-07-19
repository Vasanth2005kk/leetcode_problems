class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_descimal=int(a,2)
        b_descimal=int(b,2)
        return(bin(a_descimal+b_descimal).replace("0b",""))
    

a = "11"
b = "1"

obj=Solution().addBinary(a,b)
print(obj)

a = "1010"
b = "1011"

obj=Solution().addBinary(a,b)
print(obj)