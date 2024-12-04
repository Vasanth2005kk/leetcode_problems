
class Solution:
    def titleToNumber(self, columnTitle: str) -> int: 
        courrent = 0
        for i in columnTitle:
            ans = (courrent*26)+(ord(i)-ord("A"))+1
            courrent = ans

        return courrent


columnTitle = "A"
obj = Solution().titleToNumber(columnTitle)
print(obj)

columnTitle = "AB"
obj = Solution().titleToNumber(columnTitle)
print(obj)

columnTitle = "ZY"
obj = Solution().titleToNumber(columnTitle)
print(obj)