class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x=str(x)
        ans=string_x[::-1]
        if int(ans) == x:
            return True
        else:
            return False


x = 121
obj=Solution()
output=obj.isPalindrome(x)

print(output)