class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        chars = set(s)
        max_len = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]

                valid = True
        
                for ch in chars:
                    if sub.count(ch) > 2:
                        valid = False
                        break

                if valid:
                    max_len = max(max_len, len(sub))

        return max_len  

s = "adaddccdb"
obj = Solution().maximumLengthSubstring(s)

print(obj)

