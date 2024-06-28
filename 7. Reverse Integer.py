class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if x.startswith('-'):
            if -2**31 >int("-"+x[1::][::-1]):
                return 0
            output=x[1::][::-1]
            return int("-"+output)
        if 2**31-1 < int(x[::-1]):
            return 0
        else:
            output=x[::-1]
            return int(output)
        
x=-2147483648
obj=Solution()
output=obj.reverse(x)

print(output)
