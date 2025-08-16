class Solution:
    def firstUniqChar(self, s: str) -> int:
        output = []
        for i in set(s):
            if s.count(i) ==  1:
                output.append(s.find(i))
        
        if output:
            return min(output)
        return -1

s="leetcode"
obj = Solution().firstUniqChar(s)
print(obj)