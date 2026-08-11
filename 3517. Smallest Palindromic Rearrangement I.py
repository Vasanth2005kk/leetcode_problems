class Solution:
    def smallestPalindrome(self, s: str) -> str:
        order = [0]*26
        for i in s:
            index = ord(i)-97
            order[index] = order[index] + 1
        left = ""
        mid = ""
        for c in range(26):
            value = order[c] 
            if value != 0:
                key = chr(c+97)
                d = value //2 
                if value % 2 == 0:
                    left += key*d
                else:
                    left += key*d
                    mid += key

        return left+mid+left[::-1]
        
s = "babab"
obj = Solution().smallestPalindrome(s)
print(obj)