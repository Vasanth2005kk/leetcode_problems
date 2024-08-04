s = "hello"

'''The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.'''

class Solution:
    def scoreOfString(self, s: str) -> int:
        total=0
        for i in range(len(s)-1):
            letters=s[i:i+2]
            total+=abs(ord(letters[0])-ord(letters[1]))
        return total   
    


obj=Solution().scoreOfString(s=s)
print(obj)