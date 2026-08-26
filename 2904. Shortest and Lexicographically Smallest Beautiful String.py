class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        right = 0

        minValue = 10000
        Sumsub = 0
        output = ""

        while right < len(s):

            if s[right] == "1":
                Sumsub += 1

            while Sumsub == k:

                subString = s[left:right + 1]

                # Smaller length
                if len(subString) < minValue:
                    minValue = len(subString)
                    output = subString

                # Same length, lexicographically smaller
                elif len(subString) == minValue and subString < output:
                    output = subString

                if s[left] == "1":
                    Sumsub -= 1

                left += 1

            right += 1

        return output

        
        

s = "1011"
k = 2

s = "100011001"
k = 3


obj = Solution().shortestBeautifulSubstring(s,k)
print(obj)
