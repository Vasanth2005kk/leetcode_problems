# s = "()[]{}"
# s = "()"
# s = "(]"
s="([)]"
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or stack.pop() != c:
                return False
        return not stack


'''class Solution:
    def isValid(self, s: str) -> bool:        
        parenthesis=0
        square_brackets=0
        Curly_bracke=0

        for i in s:
            if i in list("()"):
                parenthesis+=1
            elif i in list("[]"):
                square_brackets+=1
            elif i in list("{}"):
                Curly_bracke+=1
        else:
            if parenthesis%2 == 0 and parenthesis != 0:
                return(True)
            elif square_brackets%2 == 0 and square_brackets != 0:
                return(True)
            elif Curly_bracke%2 == 0 and Curly_bracke != 0:
                return(True)
            else:
                return(False)
'''

obj=Solution().isValid(s=s)
print(obj)

