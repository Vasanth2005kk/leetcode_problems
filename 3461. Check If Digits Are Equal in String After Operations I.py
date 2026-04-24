class Solution:
    def hasSameDigits(self, s: str) -> bool:
        index = 0
        Slength =  len(s)
        numstring = ""

        while Slength > 2:
            for i in range(Slength-1):
                numstring += str((int(s[index])+int(s[index+1]))%10)
                # print(numstring)
                index += 1

            s = numstring
            Slength = len(s)
            index = 0 
            numstring = ''

        if s[0] == s[1]:
            return True
        return False
    
s = "3902"
 

obj = Solution().hasSameDigits(s)

print(obj)