class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s = "Hello World"
obj=Solution().lengthOfLastWord(s=s)
print(obj)