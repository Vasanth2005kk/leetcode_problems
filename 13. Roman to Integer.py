class Solution:
    def romanToInt(self, s: str) -> int:
        I,V,X,L,C,D,M =1,5,10,50,100,500,1000
        s=s.replace("IV","IIII").replace("CM","DCCCC").replace("XC","LXXXX")
        s=s.replace("IX","VIIII").replace("CD","CCCC").replace("XL","XXXX")
        ans=0
        for i in s:
            if i == "I":
                ans+=I
            elif i == "V":
                ans+=V
            elif i == "X":
                ans+=X
            elif i == "L":
                ans+=L
            elif i == "C":
                ans+=C
            elif i == "D":
                ans+=D
            elif i == "M":
                ans+=M

        return ans


obj=Solution().romanToInt(s="MCMXCIV")
print(obj)